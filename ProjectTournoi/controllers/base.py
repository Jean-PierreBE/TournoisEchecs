"""Define the main controller"""
import ProjectTournoi.controllers.Reports as rep
import ProjectTournoi.controllers.tournament as ctn
import ProjectTournoi.controllers.game as cgm
import ProjectTournoi.controllers.round as rnd
import ProjectTournoi.controllers.player as ply

import ProjectTournoi.variables as vr

import jsons
from tinydb import TinyDB

class Controller:
    """Main controller"""

    def __init__(self, ctview, cpview, crview, cgview, cvview):
        # models
        self.tournois = []
        self.players = []
        # views
        self.ctview = ctview
        self.cpview = cpview
        self.crview = crview
        self.cgview = cgview
        self.vview = cvview

    def run_create_players(self):
        encode_players = True
        db_players = TinyDB(vr.DB_PLAYERS)
        players_table = db_players.table(vr.DB_PLAYERS)
        print('len(db_players) : ' + str(len(db_players)))
        for row in players_table:
            print(row)
        play_seq = len(players_table)
        while encode_players:
            """Encode players"""
            play_seq += 1
            ply.create_player(self, play_seq)
            encode_players = ply.get_players_continue(self)
        serialized_players = jsons.dump(self.players)
        players_table.insert_multiple(serialized_players)

    def run_create_tournoi(self):
        """Run the game."""
        if len(self.tournois) == 0:
            pass
        """Initialize tournament"""
        ctn.create_tournament(self)
        # liste des tournois
        # demander de créer ou gérer un tournoi existant
        # tournoi = self.tournois[indice choisi]
        current_tournament = self.tournois[0]
        """Select if you want to encoe players or to choose them from a list"""
        if ply.get_players_choose(self) == 1:
            """Encode players"""
            ply.create_players(self, current_tournament)
        else:
            """choose players from a list"""
            ply.choose_players(self, current_tournament)

        """Rounds"""
        for num_round in range(vr.NUMBER_ROUNDS):
            """begin round"""
            rnd.create_round_begin(self, num_round, current_tournament)
            """Swiss algorithm"""
            cgm.get_games_swiss(self, num_round, current_tournament)
            running_game = True

            while running_game:
                """view games"""
                rep.print_turning_views(self, num_round, current_tournament)
                """choose number of game to encode or leave the round"""
                running_game, igame = cgm.get_game_choose(self, num_round)
                """encode score"""
                if running_game:
                    cgm.get_result(self, current_tournament.rounds[num_round].games[igame])
            """end round"""
            rnd.get_round_end(self, num_round, current_tournament)

        """Affichage résultat tournoi"""
        rep.print_end_views(self, current_tournament)
        """serialize object"""
        serialized_tournament = jsons.dump(current_tournament)
        db = TinyDB(vr.DB_TOURNAMENT)
        tournament_table = db.table(vr.TABLE_TOURNAMENT)
        #tournament_table.truncate()  # clear the table first
        tournament_table.insert(serialized_tournament)
        """delete self tournois after save"""
        self.tournois.clear()
