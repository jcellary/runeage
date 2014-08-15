'use strict';

/* Card set definitions */

function Card(count, imagePath, imageXOffset, imageYOffset, type, attributes, priceGold, priceInfluence) {
    this.count = count;
    this.imagePath = imagePath;
    this.imageXOffset = imageXOffset;
    this.imageYOffset = imageYOffset;
    this.type = type;
    this.attributes = attributes;
    this.priceGold = priceGold;
    this.priceInfluence = priceInfluence;
};

Card.width = 160;
Card.height = 244;

var CardAttributes = {
    IsNeutral: 1,
    IsUnit: 2,
    IsStronghold: 4,
    IsCity: 8,
    IsSpell: 16,
};

var CardTypeEnum = {
    UndeadStronghold: 0,
    UndeadReanimate: 1,
    UndeadSkeletonArcher: 2,
    UndeadDarkKnight: 3,
    UndeadNecromancer: 4,
};

var CardBuilder = {

    buildUndeadReanimate: function(count) {
        var attributes = CardAttributes.IsUnit;
        return new Card(count, 'img/cards_undead.jpg', Card.width * 1, 0, CardTypeEnum.UndeadReanimate, attributes, 1, 0);
    },
}

var CardSetCreator = {
    
    createNeutralAvalableCardSet: function() {
    
    },
    
    createUndeadAvailableCardSet: function() {
        var reanimate = CardBuilder.buildUndeadReanimate(6);
        
        return [reanimate];
    },
    
    createUndeadHandCardSet: function() {
        var reanimate = CardBuilder.buildUndeadReanimate(6);
        
        return [reanimate];
    },

};