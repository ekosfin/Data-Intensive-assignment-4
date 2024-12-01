db = db.getSiblingDB("nosql_db");
db.createCollection("locations");

db.locations.insertMany([
  { name: "Mumbai_Office", city: "Mumbai", country: "India" },
  { name: "Mexico_City_Office", city: "Mexico City", country: "Mexico" },
  { name: "Cape_Town_Office", city: "Cape Town", country: "South Africa" },
  { name: "Dubai_Office", city: "Dubai", country: "UAE" },
  { name: "Bangkok_Office", city: "Bangkok", country: "Thailand" },
]);
