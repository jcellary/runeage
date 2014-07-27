var Game = {

    welcomeScreen:
        '<H1>Welcome to RuneAge!</H1>' +
        'Please provide your name: ' +
        '<Form>' +
        '<Input Type="Text" Id="Name" />' +
        '<Input Type="Button" onclick="Game.submitWelcome()" />' +
        '</Form>',

    start: function(id) {
        this.mainPanel = $(id);

        this.loadImages();
        this.displayWelcome();
        this.runGame();


    },

    loadImages: function () {
        this.imgCardsUndead = new Image();
        this.imgCardsUndead.src = 'img/cards_undead.jpg';

        //this.imgCardsUndead1 = this.imgCardsUndead.copy;
    },

    displayWelcome: function() {
        mainPanel.clear();

        mainPanel.append(this.welcomeScreen);

    },

    submitWelecome: function() {
      this.runGame();
    },

    runGame: function() {
        mainPanel.clear();

        //mainPanel.backgroundImage = this.imgCardsUndead;
        var cardDiv = $('<div id = "card1" />').css('width', 100).css('height', 100).css('background-color', '#00ff00');
        cardDiv.append(this.imgCardsUndead);

        //cardDiv.backgroundImage = this.imgCardsUndead;
        //cardDiv.css('background', this.imgCardsUndead).css('background-position', '0, 0');

        mainPanel.append(cardDiv);

    }

};
