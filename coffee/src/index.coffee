server = require "./server"
router = require "./route"
requestHandlers = require "./requestHandlers"

handle = 
	"/" : requestHandlers.start
	"/start": requestHandlers.start
	"/upload": requestHandlers.upload
	"/show": requestHandlers.show

server.start(router.route, handle)