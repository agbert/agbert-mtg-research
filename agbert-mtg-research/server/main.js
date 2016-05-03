import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';

//Meteor.settings.public.houston_documents_per_page = 10;


//export const Cards = new Mongo.Collection('Cards');
//export const Sets = new Mongo.Collection('Sets');
export const TheTokenProject = new Mongo.Collection('TheTokenProject');
export const TheTokenProject_Cards = new Mongo.Collection('TheTokenProject_Cards');//.find({"value.tppid": {$ne: 0}});

//Houston.add_collection(Cards);
//Houston.add_collection(Sets);
Houston.add_collection(TheTokenProject);
Houston.add_collection(TheTokenProject_Cards);
Houston.add_collection(Meteor.users);
Houston.add_collection(Houston._admins);

Meteor.startup(() => {
  // code to run on server at startup
});
