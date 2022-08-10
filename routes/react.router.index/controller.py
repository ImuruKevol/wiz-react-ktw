import markupsafe

app = wiz.model("react/main")("build").load("")

view = app.fs.read.text("wiz.build.html")
view = markupsafe.Markup(view)
wiz.response.send(view, "text/html")
