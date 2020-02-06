from models.project import Project

PORTFOLIO_NAME = "Jacob Sabella"
PORTFOLIO_TITLE = "Software Developer"
PORTFOLIO_DESCRIPTION = "Software developer specializing in back-end web and batch processes. Expert in " \
                        "Java/SQL/PLSQL. Experience with web technologies such as Flask, Node.js, and Spring Boot. " \
                        "Reluctantly admitting COBOL exposure. Projects worked on in Unity3D and GIS related apps."
projects = []

projects[0] = Project("Twitics", "Given a Twitch user, show users that are not following them back.", None,
                      "https://twitics.jacobsabella.com")

projects[1] = Project("Associate Toolkit", "Android app for WalMart associates that displays barcodes for given items.",
                      None, "https://play.google.com/store/apps/details?id=com.soulworks.soulofset.associatetoolkit")

projects[2] = Project("Jacob Sabella Portfolio", "This website. Built on Flask using Bootstrap for the front end",
                      None, "https://jacobsabella.com")
