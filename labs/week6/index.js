const express = require("express")
const path = require("path")
// Imports for routers specified in routes
const aboutRouter = require("./routes/about")
const welcomeRouter = require("./routes/welcome")
const contactRouter = require("./routes/contact")
const dateRouter = require("./routes/date")
const fileRouter = require("./routes/file")
const chainRouter = require("./routes/chain")
const indexRouter = require("./routes/index")

const app = express();

const port = 8000;

// Routers middleware, relative parts of the url can be found in their respective views files, the first argument specifies 
// where the the relative parts need to be appened to. For instane, if we changed app.use("/about", aboutRouter) to app.use("/information", aboutRouter)
// then the secret about file would be found by accessing localhost:800/information/secret as opposed to localhost:8000/about/secret
app.use("/", indexRouter)
app.use("/about", aboutRouter)
app.use("/welcome", welcomeRouter)
app.use("/contact", contactRouter)
app.use("/date", dateRouter)
app.use("/file", fileRouter)
app.use("/chain", chainRouter)

// Tells our application to listen to requests on specified port
app.listen(port, () => console.log(`Server is running on port ${port}`))