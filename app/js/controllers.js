'use strict';

/* Controllers */

angular.module('runeAge.controllers', [])
    .controller('WelcomeCtrl', ['$scope', '$location', function($scope, $location) {

        $scope.startGame = function() {
            //$scope.playerName;
            //#/welcome
            $location.path("/game");
        }
    }])
    .controller('GameCtrl', ['$scope', function($scope) {

    }]);
