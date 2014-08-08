var Game = {

    main: function(id) {
        View.mainPanel = $(id);

        View.loadImages();
        View.displayWelcome();
    },

    startGame: function() {
    
        View.displayGame();
    }
};

var View = {

    welcomeTemplate:
        '<div id="WelcomeScreen">' +
        '<br>' +
        '<h1>Welcome to Rune Age!</h1>' +
        'Please provide your name: ' +
        '<form>' +
        '<input type="Text" id="TextName" />' +
        '<input type="Button" value="Start" id="ButtonStart" />' +
        '</form>' +
        '</div>',

    gameTemplate:
        '',
        
    displayView: function(template) {
        this.mainPanel.html('');
        this.mainPanel.append(template);
    
    },

    displayWelcome: function() {
        this.displayView(this.welcomeTemplate);
        
        $('#ButtonStart').click(function() { Game.startGame(); });
    },
    
    displayGame: function() {
        this.displayView(this.gameTemplate);
        
        var cardDiv = $('<div id = "card1" />').css('width', 160).css('height', 244);
        cardDiv.css('background-image', 'url(' + this.imgCardsUndead.src + ')').css('background-position', '-320px 0px');

        this.mainPanel.append(cardDiv);
    },

    loadImages: function () {
        this.imgCardsUndead = new Image();
        this.imgCardsUndead.src = 'img/cards_undead.jpg';
    },
}