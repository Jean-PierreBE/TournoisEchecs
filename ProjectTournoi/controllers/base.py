"""Define the main controller"""
import ProjectTournoi.controllers.Reports as rep
import ProjectTournoi.controllers.tournament as ctn
import ProjectTournoi.controllers.game as cgm
import ProjectTournoi.controllers.round as rnd
import ProjectTournoi.controllers.player as ply

from ProjectTournoi.views import createendview as cv
from ProjectTournoi.views import createplayer as cp
from ProjectTournoi.views import createtournament as ct
from ProjectTournoi.variables import NUMBER_ROUNDS
import ProjectTournoi.controllers.acces_db as db

from ProjectTournoi.db import db_players, db_tournament


class Controller:
    """Main controller"""

    def __init__(self, ctview, cpview, crview, cgview, cvview):
        # models
        self.tournaments = []
        self.players = []
        self.current_tournament = ''
        # views
        self.ctview = ctview
        self.cpview = cpview
        self.crview = crview
        self.cgview = cgview
        self.vview = cvview

    def run_create_players(self):
        encode_players = True
        play_seq = len(db_players)
        while encode_players:
            """Encode players"""
            play_seq += 1
            ply.create_player(self, play_seq)
            encode_players = ply.get_players_continue(self)
        db.insert_players(self.players)
        self.players.clear()

    def run_update_players(self):
        encode_players = True
        players = db.download_players()
        cv.CreateEndView.list_only_players(self, players)
        while encode_players:
            """Encode players"""
            num_play = cp.CreatePlayer.prompt_choose_indice_players(self, -1, len(players))
            player_out = ply.update_player(self, players[num_play-1])
            db.update_player(player_out)
            encode_players = ply.get_players_continue(self)

    def run_update_tournoi(self):
        # list of tournaments
        update_tournament = True
        while update_tournament:
            self.tournaments = db.download_tournaments()
            cv.CreateEndView.list_only_tournaments(self, self.tournaments)
            """Choose tournament"""
            ind_tournament = ct.CreateTournament.prompt_choose_tournament(self, len(self.tournaments))
            tournament = self.tournaments[ind_tournament - 1]
            """check previous results"""
            cv.CreateEndView.list_results_rounds(self, tournament)
            """choose round to restart"""
            round_deb = ct.CreateTournament.prompt_choose_round_deb(self, len(tournament.rounds))
            """delete rounds if replayed"""
            for indc in range(round_deb - 1, len(tournament.rounds)):
                del tournament.rounds[round_deb - 1]
            """update results tournament"""
            ply.update_score_if_replay(self, tournament)
            """execute tournament"""
            running_tournament = True
            while running_tournament:
                for num_round in range(round_deb - 1, NUMBER_ROUNDS):
                    """begin round"""
                    rnd.create_round_begin(self, num_round, tournament)
                    """Swiss algorithm"""
                    cgm.get_games_swiss(self, num_round, tournament)
                    running_game = True
                    while running_game:
                        """view games"""
                        rep.print_turning_views(self, num_round, tournament)
                        """choose number of game to encode or leave the round"""
                        running_game, igame = cgm.get_game_choose(self, num_round)
                        """encode score"""
                        if running_game:
                            cgm.get_result(self, tournament.rounds[num_round].games[igame])
                    """end round"""
                    rnd.get_round_end(self, num_round, tournament)
                    """select if you want to continue tournament or yes"""
                    if num_round == NUMBER_ROUNDS - 1:
                        running_tournament = False
                    else:
                        running_tournament = ctn.choose_continue_tournament(self)
                    if running_tournament is False:
                        break
                """Affichage résultat tournoi"""
                rep.print_end_views(self, tournament)
                """serialize object"""
                db.update_tournament(tournament)
            update_tournament = ctn.continue_another_tournament(self)

    def run_create_tournoi(self):
        ctn.create_tournament(self, len(db_tournament))
        """choose players from a list"""
        ply.choose_players(self, self.current_tournament)
        """Tournament"""
        running_tournament = True
        """Rounds"""
        for num_round in range(NUMBER_ROUNDS):
            """begin round"""
            rnd.create_round_begin(self, num_round, self.current_tournament)
            """Swiss algorithm"""
            cgm.get_games_swiss(self, num_round, self.current_tournament)
            running_game = True

            while running_game:
                """view games"""
                rep.print_turning_views(self, num_round, self.current_tournament)
                """choose number of game to encode or leave the round"""
                running_game, igame = cgm.get_game_choose(self, num_round)
                """encode score"""
                if running_game:
                    cgm.get_result(self, self.current_tournament.rounds[num_round].games[igame])
            """end round"""
            rnd.get_round_end(self, num_round, self.current_tournament)
            """select if you want to continue tournament or yes"""
            if num_round == NUMBER_ROUNDS - 1:
                running_tournament = False
            else:
                running_tournament = ctn.choose_continue_tournament(self)
            if running_tournament is False:
                break

        """Affichage résultat tournoi"""
        rep.print_end_views(self, self.current_tournament)
        """insert tournament in db"""
        db.insert_tournament(self.current_tournament)

    def run_report_players_alph(self):
        """reports"""
        rep.print_players_order_alphabetics(self)

    def run_report_players_classment(self):
        rep.print_players_order_classment(self)

    def run_report_tournament(self):
        rep.print_all_tournaments(self)
