import dash

app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True
app.title='Dashboard'
app.update_interval=30