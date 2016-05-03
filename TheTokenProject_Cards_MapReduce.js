var mapUsers, mapComments, reduce;

db.TheTokenProject_Cards.remove({});


mapTheTokenProject = function() {
    emit(this.name, {
    	  tppid: this.id,
        name: this.name,
        count: this.count,
        foil: this.foil,
        cardData: 0
    });
};
mapCards = function() {
	  var cardDataA = {};
	  var field;
	  for (field in this) {
  		cardDataA[field] = this[field];
	  }
	  var value = {
    	  tppid: 0,
        name: this.name,
        count: 0,
        foil: 0,
        cardData: cardDataA
		}	  	
    emit(this.name, value);
};
reduce = function(k, values) {
		var result = {
			tppid: 0,
			name: 0,
			count: 0,
			foil: 0,
			cardData: 0
			};
    values.forEach(function(value) {
      for (field in value) {
    	  if (result[field] === 0 && value[field] !== null && value[field] !== 0) {
          result[field] = value[field];
        }
      }
    });
    return result;
};
db.TheTokenProject.mapReduce(mapTheTokenProject, reduce, {"out": {"reduce": "TheTokenProject_Cards"}});
db.Cards.mapReduce(mapCards, reduce, {"out": {"reduce": "TheTokenProject_Cards"}});
db.TheTokenProject_Cards.find({}).pretty(); // see the resulting collection

db.TheTokenProject_Cards.remove({"value.tppid":0});
