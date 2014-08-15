'use strict';

/* Controllers */

angular.module('runeAge.controllers', [])
    .controller('WelcomeCtrl', ['$scope', '$location', function($scope, $location) {

        $scope.playerName = '',
    
        $scope.startGame = function() {
            //$scope.playerName;
            //#/welcome
            if ($scope.playerName.length > 0)
                $location.path("/game");
            else 
                $('#PlayerNameValidationError').css('visibility', 'visible');
        }
    }])
    .controller('GameCtrl', ['$scope', function($scope) {

        $scope.availablePlayerCardSets = CardSetCreator.createUndeadAvailableCardSet();
    
    }]);
