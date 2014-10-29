/*
*   Usage: var gcjloc = transformFromWGSToGCJ(lng,lat);
*   Source: https://github.com/hiwanz/wgs2mars.js.git
*/
(function(global){
    // const PI
    var PI = 3.14159265358979324;
    // Krasovsky 1940
    //
    // a = 6378245.0, 1/f = 298.3
    // b = a * (1 - f)
    // ee = (a^2 - b^2) / a^2;
    var a = 6378245.0;
    var ee = 0.00669342162296594323;

    function Rectangle(lat1, lng1, lat2, lng2) {
        this.East = Math.max(lng1, lng2);
        this.South = Math.min(lat1, lat2);
        this.West = Math.min(lng1, lng2);
        this.North = Math.max(lat1, lat2);
    }

    function IsInRect(rect, lat, lon) {
        return rect.West <= lon && rect.East >= lon && rect.North >= lat && rect.South <= lat;
    }

    var region = [
        new Rectangle(49.220400, 79.446200, 42.889900, 96.330000),
        new Rectangle(54.141500, 109.687200, 39.374200, 135.000200),
        new Rectangle(42.889900, 73.124600, 29.529700, 124.143255),
        new Rectangle(29.529700, 82.968400, 26.718600, 97.035200),
        new Rectangle(29.529700, 97.025300, 20.414096, 124.367395),
        new Rectangle(20.414096, 107.975793, 17.871542, 111.744104)
    ];
    var exclude = [
        new Rectangle(25.398623, 119.921265, 21.785006, 122.497559),
        new Rectangle(22.284000, 101.865200, 20.098800, 106.665000),
        new Rectangle(21.542200, 106.452500, 20.487800, 108.051000),
        new Rectangle(55.817500, 109.032300, 50.325700, 119.127000),
        new Rectangle(55.817500, 127.456800, 49.557400, 137.022700),
        new Rectangle(44.892200, 131.266200, 42.569200, 137.022700)
    ];

    function IsInChina(lat, lon) {
        for (var i = 0; i < region.length; i++) {
            if (IsInRect(region[i], lat, lon))
            {
                for (var j = 0; j < exclude.length; j++)
                {
                    if (IsInRect(exclude[j], lat, lon))
                    {
                        return false;
                    }
                }
                return true;
            }
        }
        return false;
    }

    function transformLat(x, y){
        var ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * Math.sqrt(Math.abs(x));
        ret += (20.0 * Math.sin(6.0 * x * PI) + 20.0 * Math.sin(2.0 * x * PI)) * 2.0 / 3.0;
        ret += (20.0 * Math.sin(y * PI) + 40.0 * Math.sin(y / 3.0 * PI)) * 2.0 / 3.0;
        ret += (160.0 * Math.sin(y / 12.0 * PI) + 320 * Math.sin(y * PI / 30.0)) * 2.0 / 3.0;
        return ret;
    }

    function transformLon(x, y){
        var ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * Math.sqrt(Math.abs(x));
        ret += (20.0 * Math.sin(6.0 * x * PI) + 20.0 * Math.sin(2.0 * x * PI)) * 2.0 / 3.0;
        ret += (20.0 * Math.sin(x * PI) + 40.0 * Math.sin(x / 3.0 * PI)) * 2.0 / 3.0;
        ret += (150.0 * Math.sin(x / 12.0 * PI) + 300.0 * Math.sin(x / 30.0 * PI)) * 2.0 / 3.0;
        return ret;
    }

    // World Geodetic System ==> Mars Geodetic System
    function transform(wgLon,wgLat){
        var mgLoc = {};
        if (!IsInChina(wgLat, wgLon)){
            mgLoc = {
                lat: wgLat,
                lng: wgLon
            };
            return mgLoc;
        }
        var dLat = transformLat(wgLon - 105.0, wgLat - 35.0);
        var dLon = transformLon(wgLon - 105.0, wgLat - 35.0);
        var radLat = wgLat / 180.0 * PI;
        var magic = Math.sin(radLat);
        magic = 1 - ee * magic * magic;
        var sqrtMagic = Math.sqrt(magic);
        dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * PI);
        dLon = (dLon * 180.0) / (a / sqrtMagic * Math.cos(radLat) * PI);
        mgLoc = {
            lat: wgLat + dLat,
            lng: wgLon + dLon
        };
            return mgLoc;
    }

    global.transformFromWGSToGCJ = transform;
})(window);