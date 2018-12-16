from flask import render_template
import connexion
import logging
import unicornhat as uh



# create the application instance
app = connexion.App(__name__, specification_dir="./")

# Cead the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")


if __name__ == "__main__":
    logging.info('Server stating') 
    uh.set_layout(uh.PHAT)
    uh.brightness(0.5)
    app.run(debug=True)

