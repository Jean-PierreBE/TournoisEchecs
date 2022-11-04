from ProjectTournoi.controllers.base import Controller
import ProjectTournoi.views.createtournament as vc

view = vc.CreateTournament()
game = Controller(view)

game.run()