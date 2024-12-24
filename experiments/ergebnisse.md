# Truths
## Beispiel 1 105869
{ 
  "objekte": [ 
    { 
      "flaeche": 100, 
      "verkehrswert": 63000, 
      "typ": "Wohnung", 
      "baujahr": 1924, 
      "heizsystem": null, 
      "raeume": 4, 
      "raum_typen": [ 
        "Wohnzimmer", 
        "Schlafzimmer", 
        "Küche", 
        "Badezimmer" 
      ], 
      "balkon": false, 
      "garten": false 
    } 
  ], 
  "gesamtverkehrswert": 63000 
}

## Beispiel 2 113772
{  
  "objekte": [  
    {  
      "flaeche": 55,  
      "verkehrswert": 283000,  
      "typ": "Wohnung",  
      "baujahr": 1959,  
      "heizsystem": null,  
      "raeume": null,  
      "raum_typen": [],  
      "balkon": false,  
      "garten": true  
    }  
  ],  
  "gesamtverkehrswert": 283000  
}

## Beispiel 3 127734
{ 
    "objekte": [ 
        { 
        "flaeche": 921, 
        "verkehrswert": 88000, 
        "typ": "Anderer", 
        "baujahr": null, 
        "heizsystem": null, 
        "raeume": null, 
        "raum_typen": [], 
        "balkon": false, 
        "garten": false 
        } 
    ], 
    "gesamtverkehrswert": 88000 
}

## Beispiel 4 15125
{ "objekte": [ { "typ": "Haus", "flaeche": 208, "verkehrswert": 125000, "baujahr": null, "heizsystem": null, "raeume": null, "raum_typen": [], "balkon": false,"garten": false } ], "gesamtverkehrswert": 125000 }

## Beispiel 5 27138
{  "objekte": [ {  "raeume": 3,  "balkon": false,  "raum_typen": [], "baujahr": 1966, "heizsystem": null,  "typ": "Wohnung",  "flaeche": 66,  "garten": false,  "verkehrswert": 99000  } ],  "gesamtverkehrswert": 99000 }

## Beispiel 6 359816
{ 
    "objekte": [ 
        { 
          "typ": "Wohnung", 
          "baujahr": 1897, 
          "flaeche": 120, 
          "raeume": 4, 
          "raum_typen": [], 
          "balkon": false, 
          "garten": false, 
          "heizsystem": null, 
          "verkehrswert": 87600 
        } 
    ], 
    "gesamtverkehrswert": 87600 
}

## Beispiel 7 60782
{ "objekte": [ { "flaeche": 67, "verkehrswert": 250000, "typ": "Wohnung", "baujahr": 1900, "heizsystem": "Gas", "raeume": 2, "raum_typen": [ "Wohnzimmer", "Küche" ], "balkon": true, "garten": false }, { "flaeche": 64, "verkehrswert": 240000, "typ": "Wohnung", "baujahr": 1900, "heizsystem": "Gas", "raeume": 2, "raum_typen": ["Badezimmer", "Hauswirtschaftsraum", "Flur" ], "balkon": false, "garten": false } ], "gesamtverkehrswert": 580000 } 

## Beispiel 8 61344
{
  "objekte": [
    {
      "flaeche": 62,
      "verkehrswert": 258000,
      "typ": "Wohnung",
      "baujahr": null,
      "heizsystem": null,
      "raeume": 2,
      "raum_typen": [
        "Küche",
        "Badezimmer"
      ],
      "balkon": true,
      "garten": false
    }
  ],
  "gesamtverkehrswert": 258000
}

## Beispiel 9 8033
{ "objekte": [ { "flaeche": 918, "verkehrswert": 139000, "typ": "Anderes", "baujahr": null, "heizsystem": null, "raeume": null, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 139000 } 

## Beispiel 10 8786
{ "objekte": [ { "flaeche": 66, "typ": "Haus", "verkehrswert": 285000, "raeume": null, "baujahr": 2000, "heizsystem": null, "raum_typen": [], "balkon": false, "garten": true}],  "gesamtverkehrswert": 285000 }  

# 0shot

## Beispiel 1
{ 
  "objekte": [ 
    { 
      "flaeche": 845, 
      "verkehrswert": 63000, 
      "typ": "Wohnung", 
      "baujahr": 1924, 
      "heizsystem": "Gas", 
      "raeume": 4, 
      "raum_typen": [ 
        "Wohnzimmer", 
        "Schlafzimmer", 
        "Küche", 
        "Badezimmer" 
      ], 
      "balkon": false, 
      "garten": false 
    } 
  ], 
  "gesamtverkehrswert": 63000 
} 

## Beispiel 2
{  
  "objekte": [  
    {  
      "flaeche": 55,  
      "verkehrswert": 283000,  
      "typ": "Wohnung",  
      "baujahr": 1959,  
      "heizsystem": "Gas",  
      "raeume": 5,  
      "raum_typen": [  
        "Wohnzimmer",  
        "Schlafzimmer",  
        "Küche",  
        "Badezimmer",  
        "Arbeitszimmer"  
      ],  
      "balkon": false,  
      "garten": true  
    }  
  ],  
  "gesamtverkehrswert": 283000  
}

## Beispiel 3
{ 
    "objekte": [ 
        { 
        "flaeche": 921, 
        "verkehrswert": 88000, 
        "typ": "Wohnung", 
        "baujahr": null, 
        "heizsystem": "Gas", 
        "raeume": 8, 
        "raum_typen": [ 
          "Wohnzimmer", 
          "Schlafzimmer", 
          "Küche", 
          "Badezimmer", 
          "Arbeitszimmer", 
          "Flur", 
          "Abstellraum", 
          "Esszimmer" 
        ], 
        "balkon": false, 
        "garten": false 
        } 
    ], 
    "gesamtverkehrswert": 88000 
}

## Beispiel 4
{ "objekte": [ { "typ": "Haus", "flaeche": 208, "verkehrswert": 125000, "baujahr": null, "heizsystem": null, "raeume": 1, "raum_typen": [], "balkon": false,"garten": false } ], "gesamtverkehrswert": 125000 } 

## Beispiel 5
{  "objekte": [ {  "raeume": 3,  "balkon": false,  "raum_typen": [ "Wohnzimmer", "Schlafzimmer", "Küche", "Badezimmer" ], "baujahr": 1966, "heizsystem": "Elektrische Heizung",  "typ": "Wohnung",  "flaeche": 66,  "garten": false,  "verkehrswert": 99000  } ],  "gesamtverkehrswert": 99000 }

## Beispiel 6
{ 
    "objekte": [ 
        { 
          "typ": "Wohnung", 
          "baujahr": 1897, 
          "flaeche": 120, 
          "raeume": 4, 
          "raum_typen": ["Wohnzimmer", "Küche", "Badezimmer", "Badezimmer"], 
          "balkon": false, 
          "garten": false, 
          "heizsystem": "Fernwärme", 
          "verkehrswert": 87600 
        } 
    ], 
    "gesamtverkehrswert": 87600 
}

## Beispiel 7
{ "objekte": [ { "flaeche": 67, "verkehrswert": 250000, "typ": "Wohnung", "baujahr": 1900, "heizsystem": "Gas", "raeume": 2, "raum_typen": [ "Wohnzimmer", "Küche" ], "balkon": true, "garten": false }, { "flaeche": 64, "verkehrswert": 20224, "typ": "Anderes", "baujahr": "ca. 1900", "heizsystem": "Gas", "raeume": 4, "raum_typen": [ "Schlafzimmer", "Badezimmer", "Hauswirtschaftsraum", "Flur" ], "balkon": false, "garten": false } ], "gesamtverkehrswert": 580000 } 

## Beispiel 8
{
  "objekte": [
    {
      "flaeche": 62,
      "verkehrswert": 258000,
      "typ": "Wohnung",
      "baujahr": null,
      "heizsystem": "Strom",
      "raeume": 2,
      "raum_typen": [
        "Badezimmer",
        "Badezimmer"
      ],
      "balkon": true,
      "garten": false
    }
  ],
  "gesamtverkehrswert": 258000
}

## Beispiel 9
{ "objekte": [ { "flaeche": 918, "verkehrswert": 139000, "typ": "Anderes", "baujahr": null, "heizsystem": null, "raeume": 12, "raum_typen": ["Wohnzimmer", "Schlafzimmer", "Küche", "Badezimmer", "Arbeitszimmer", "Hauswirtschaftsraum", "Flur", "Abstellraum", "Esszimmer"], "balkon": true, "garten": false } ], "gesamtverkehrswert": 139000 } 

## Beispiel 10
{ "objekte": [ { "flaeche": 660, "typ": "Wohnung", "verkehrswert": 285000, "raeume": 5, "baujahr": 2000, "heizsystem": "Zentralheizung", "raum_typen": ["Wohnzimmer", "Badezimmer", "Schlafzimmer", "Küche", "Hauswirtschaftsraum"], "balkon": true, "garten": false}],  "gesamtverkehrswert": 285000 } 

# 1shot
## Beispiel 1
{ "objekte": [ { "raeume": 4, "baujahr": 1924, "heizsystem": null, "typ": "Wohnung", "flaeche":100, "balkon": false, "garten": false, "verkehrswert": 63000 } ], "gesamtverkehrswert": 63000 } 
 
## Beispiel 2
{ "objekte": [ { "flaeche": 64, "raeume": 3, "typ": "Wohnung", "baujahr": 1959, "raum_typen": ["Wohnzimmer", "Schlafzimmer", "Küche", "Badezimmer"], "verkehrswert": 283000, "balkon": false, "garten": false, "heizsystem": null } ], "gesamtverkehrswert": 283000 } 
 
## Beispiel 3
{
  "objekte": [
    {
      "raeume": null,
      "balkon": false,
      "raum_typen": [],
      "baujahr": null,
      "heizsystem": null,
      "typ": "Anderes",
      "flaeche": 921,
      "garten": false,
      "verkehrswert": 88000
    }
  ],
  "gesamtverkehrswert": 88000
}

## Beispiel 4
{
  "objekte": [
    {
      "raeume": null,
      "balkon": false,
      "raum_typen": [],
      "baujahr": null,
      "heizsystem": null,
      "typ": "Anderes",
      "flaeche": 208,
      "garten": false,
      "verkehrswert": 125000
    }
  ],
  "gesamtverkehrswert": 125000
}

## Beispiel 5
{ "objekte": [ { "raeume": 3, "baujahr": 1966, "flaeche": 66, "garten": false, "typ": "Wohnung", "verkehrswert": 99000, "heizsystem": null, "balkon": false, "raum_typen": [] } ], "gesamtverkehrswert": 99000 } 

## Beispiel 6
{ "objekte": [ { "flaeche": 120, "raeume": 6, "typ": "Wohnung", "baujahr": 1897, "verkehrswert": 87600, "heizsystem": null, "balkon": false, "garten": false, "raum_typen": [] } ], "gesamtverkehrswert": 87600 } 
   
## Beispiel 7
{  "objekte": [ {  "raeume": 3,  "balkon": false,  "raum_typen": [ "Wohnzimmer", "Badezimmer", "Hauswirtschaftsraum", "Flur", "Esszimmer" ], "baujahr": 1900, "heizsystem": "Gas", "typ": "Anderes", "flaeche": 64,  "garten": false, "verkehrswert": 240000  }, {  "raeume": 3,  "balkon": false,  "raum_typen": [ "Wohnzimmer", "Badezimmer", "Hauswirtschaftsraum", "Flur", "Esszimmer" ], "baujahr": 1900, "heizsystem": "Gas", "typ": "Anderes", "flaeche": 67,  "garten": false, "verkehrswert": 250000  } ],  "gesamtverkehrswert": 580000 } 
 
## Beispiel 8
  { "objekte": [ {  "raeume": 2,  "balkon": true,  "raum_typen": ["Wohnzimmer", "Küche", "Badezimmer", "Abstellraum", "Flur"],  "baujahr": null,  "heizsystem": null,  "typ": "Wohnung",  "flaeche": 62,  "garten": false,  "verkehrswert": 258000 } ],  "gesamtverkehrswert": 258000 } 

## Beispiel 9
{  
  "objekte": [  
    {  
      "baujahr": null,  
      "balkon": false,  
      "raeume": null,  
      "raum_typen": [],  
      "flaeche": 918,  
      "garten": false,  
      "verkehrswert": 139000,  
      "typ": "Anderes",  
      "heizsystem": null  
    }  
  ],  
  "gesamtverkehrswert": 139000  
} 

## Beispiel 10
{ 
  "objekte": [ 
    { 
      "raeume": 66, 
      "balkon": false, 
      "raum_typen": [], 
      "baujahr": 2000, 
      "heizsystem": null, 
      "typ": "Anderes", 
      "flaeche": 660, 
      "garten": false, 
      "verkehrswert": 285000 
    } 
  ], 
  "gesamtverkehrswert": 285000 
} 
 
# 3shot
## Beispiel 1
{ "objekte": [ { "flaeche": 100, "verkehrswert": 63000, "typ": "Wohnung", "baujahr": 1924, "heizsystem": null, "raeume": null, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 63000 } 

## Beispiel 2
{
  "objekte": [
    {
      "flaeche": 0,
      "verkehrswert": 283000,
      "typ": "Anderes",
      "baujahr": 1959,
      "heizsystem": null,
      "raeume": null,
      "raum_typen": [],
      "balkon": false,
      "garten": false
    }
  ],
  "gesamtverkehrswert": 283000
} 

## Beispiel 3
{ "objekte": [ { "flaeche": 921, "verkehrswert": 88000, "typ": "Wohnung", "baujahr": null, "heizsystem": null, "raeume": null, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 88000 } 

## Beispiel 4
{ "objekte": [ { "raeume": null, "raum_typen": [], "balkon": false, "baujahr": null, "heizsystem": null, "typ": "Anderes", "flaeche": 208, "verkehrswert": 125000, "garten": false } ], "gesamtverkehrswert": 125000 } 

## Beispiel 5
{ "objekte": [ { "flaeche": 66, "verkehrswert": 99000, "typ": "Wohnung", "baujahr": 1966, "heizsystem": null, "raeume": 3, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 99000 } 

## Beispiel 6
{ "objekte": [ { "flaeche": 120, "verkehrswert": 87600, "typ": "Wohnung", "baujahr": 1897, "heizsystem": null, "raeume": 5, "raum_typen": [ "Wohnzimmer", "Schlafzimmer", "Küche", "Badezimmer", "Abstellraum" ], "balkon": false, "garten": false } ], "gesamtverkehrswert": 87600 } 
 
## Beispiel 7
{ "objekte": [ { "flaeche": 67, "verkehrswert": 250000, "typ": "Wohnung", "baujahr": 1900, "heizsystem": "Gas", "raeume": 2, "raum_typen": [ "Wohnzimmer", "Küche" ], "balkon": true, "garten": false }, { "flaeche": 64, "verkehrswert": 240000, "typ": "Wohnung", "baujahr": 1900, "heizsystem": "Gas", "raeume": 2, "raum_typen": ["Badezimmer", "Hauswirtschaftsraum", "Flur" ], "balkon": false, "garten": false } ], "gesamtverkehrswert": 580000 } 

## Beispiel 8
{ "objekte": [ { "flaeche": 62, "verkehrswert": 258000, "typ": "Wohnung", "baujahr": null, "heizsystem": null, "raeume": 3, "raum_typen": ["Badezimmer", "Küche", "Abstellraum"], "balkon": true, "garten": false } ], "gesamtverkehrswert": 258000 } 

## Beispiel 9
{ "objekte": [ { "flaeche": 918, "verkehrswert": 139000, "typ": "Anderes", "baujahr": null, "heizsystem": null, "raeume": null, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 139000 } 

## Beispiel 10
{ "objekte": [ { "flaeche": 74, "verkehrswert": 285000, "typ": "Anderes", "baujahr": null, "heizsystem": null, "raeume": null, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 285000 } 

# 5shot
## Beispiel 1
{ "objekte": [ { "flaeche": 100, "verkehrswert": 63000, "typ": "Wohnung", "baujahr": 1924,"heizsystem": null, "raeume": 4, "raum_typen": [ "Wohnzimmer", "Küche", "Badezimmer","Abstellraum" ], "balkon": false, "garten": false } ], "gesamtverkehrswert": 63000 } 

## Beispiel 2
{ "objekte": [ { "flaeche": 25, "verkehrswert": 283000, "typ": "Wohnung", "baujahr": 1959, "heizsystem": null, "raeume": 3, "raum_typen": ["Wohnzimmer", "Küche", "Badezimmer"], "balkon": false, "garten": true}],  "gesamtverkehrswert": 283000 } 

## Beispiel 3
{ "objekte": [ { "flaeche": 921, "verkehrswert": 88000, "typ": "Haus", "baujahr": null, "heizsystem": null, "raeume": null, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 88000 } 

## Beispiel 4
{ "objekte": [ { "typ": "Haus", "flaeche": 208, "verkehrswert": 125000, "baujahr": null, "heizsystem": null, "raeume": null, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 125000 } 

## Beispiel 5
{ "objekte": [ { "flaeche": 66, "verkehrswert": 99000, "typ": "Wohnung", "baujahr": 1966, "heizsystem": null, "raeume": 3, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 99000 } 

## Beispiel 6
{ "objekte": [ { "flaeche": 195, "verkehrswert": 87600, "typ": "Wohnung", "baujahr": 1897, "heizsystem": null, "raeume": 4, "raum_typen": [ "Küche", "Badezimmer", "Abstellraum", "Wohnzimmer" ], "balkon": false, "garten": false } ], "gesamtverkehrswert": 87600 } 

## Beispiel 7
{
"objekte": [
{
"flaeche": 67,
"raeume": 2,
"raum_typen": ["Wohnzimmer", "Küche"],
"verkehrswert": 250000,
"typ": "Wohnung",
"balkon": true,
"garten": false,
"heizsystem": "Gas",
"baujahr": 1900
},
{
"flaeche": 64,
"raeume": 3,
"raum_typen": ["Badezimmer", "Hauswirtschaftsraum", "Flur"],
"verkehrswert": 240000,
"typ": "Wohnung",
"balkon": false,
"garten": false,
"heizsystem": "Gas",
"baujahr": 1900
}
],
"gesamtverkehrswert": 580000
} 

## Beispiel 8
{ "objekte": [ { "flaeche": 62, "verkehrswert": 258000, "typ": "Wohnung", "baujahr": null, "heizsystem": null, "raeume": 2, "raum_typen": ["Badezimmer", "Küche"], "balkon": true, "garten": false } ], "gesamtverkehrswert": 258000 } 

## Beispiel 9
{ "objekte": [ { "flaeche": 108, "verkehrswert": 139000, "typ": "Anderes", "baujahr": null, "heizsystem": null, "raeume": null, "raum_typen": [], "balkon": false, "garten": false } ], "gesamtverkehrswert": 139000 } 
 
## Beispiel 10
{ "objekte": [ { "flaeche": 66, "typ": "Haus", "verkehrswert": 285000, "raeume": null, "baujahr": 2000, "heizsystem": null, "raum_typen": [], "balkon": false, "garten": true } ], "gesamtverkehrswert": 285000 } 
