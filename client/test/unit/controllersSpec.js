'use strict';

/* jasmine specs for controllers go here */

describe('controllers', function(){
    beforeEach(module('runeAge.controllers'));


    it('should ....', inject(function($controller) {
        //spec body
        var welcomeCtrl = $controller('WelcomeCtrl', { $scope: {} });
        expect(welcomeCtrl).toBeDefined();
    }));

    it('should ....', inject(function($controller) {
        //spec body
        var gameCtrl = $controller('GameCtrl', { $scope: {} });
        expect(gameCtrl).toBeDefined();
    }));
});
