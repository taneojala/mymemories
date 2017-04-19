First:
- RDF presentation of TIME which is completely generic
- covering point in time, period (start TIME, end TIME) , precise TIME (datetime), unprecise TIME (e.g. year, 
month-year, season-year, decade, century)

TIME can then be used by persons (foaf), events (historical events, myMemories). Maybe the time vocabulary 
https://www.w3.org/TR/owl-time/ (instant and interval)

PLACE is needed as well: lat-long, place name, hierarchy needed: country - city - ... + lat-long. Geonames is probably 
the best to start with: gn: http://www.geonames.org/ontology

<rdf:RDF 
	xmlns:cc="http://creativecommons.org/ns#" 
	xmlns:dcterms="http://purl.org/dc/terms/" 
	xmlns:foaf="http://xmlns.com/foaf/0.1/" 
	xmlns:gn="http://www.geonames.org/ontology#" 
	xmlns:owl="http://www.w3.org/2002/07/owl#" 
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
	xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" 
	xmlns:wgs84_pos="http://www.w3.org/2003/01/geo/wgs84_pos#">
<gn:Feature rdf:about="http://sws.geonames.org/3020251/">
  <rdfs:isDefinedBy rdf:resource="http://sws.geonames.org/3020251/about.rdf"/>
  <gn:name>Embrun</gn:name>
  <gn:alternateName xml:lang="oc">Ambrun</gn:alternateName>
  <gn:featureClass rdf:resource="http://www.geonames.org/ontology#P"/>
  <gn:featureCode rdf:resource="http://www.geonames.org/ontology#P.PPL"/>
  <gn:countryCode>FR</gn:countryCode>
  <gn:population>7069</gn:population> - not used
  <gn:postalCode>05200</gn:postalCode> - not used
  <gn:postalCode>05201</gn:postalCode> - not used
  <gn:postalCode>05202</gn:postalCode> - not used
  <gn:postalCode>05208</gn:postalCode> - not used
  <gn:postalCode>05209</gn:postalCode> - not used
  <wgs84_pos:lat>44.56387</wgs84_pos:lat>
  <wgs84_pos:long>6.49526</wgs84_pos:long>
  <gn:parentFeature rdf:resource="http://sws.geonames.org/6446638/"/> - ??
  <gn:parentCountry rdf:resource="http://sws.geonames.org/3017382/"/> - ??
  <gn:parentADM1 rdf:resource="http://sws.geonames.org/2985244/"/> - not used
  <gn:parentADM2 rdf:resource="http://sws.geonames.org/3013738/"/> - not used
  <gn:parentADM3 rdf:resource="http://sws.geonames.org/3016701/"/> - not used
  <gn:parentADM4 rdf:resource="http://sws.geonames.org/6446638/"/> - not used
  <gn:nearbyFeatures rdf:resource="http://sws.geonames.org/3020251/nearby.rdf"/> - not used
  <gn:locationMap rdf:resource="http://www.geonames.org/3020251/embrun.html"/> - not used
  <gn:wikipediaArticle rdf:resource="http://de.wikipedia.org/wiki/Embrun"/>
  <gn:wikipediaArticle rdf:resource="http://en.wikipedia.org/wiki/Embrun%2C_Hautes-Alpes"/>
  <owl:seeAlso rdf:resource="http://dbpedia.org/resource/Embrun%2C_Hautes-Alpes"/>
  <gn:wikipediaArticle rdf:resource="http://fr.wikipedia.org/wiki/Embrun_%28Hautes-Alpes%29"/>
  <gn:wikipediaArticle rdf:resource="http://it.wikipedia.org/wiki/Embrun"/>
  <gn:wikipediaArticle rdf:resource="http://nl.wikipedia.org/wiki/Embrun"/>
  <gn:wikipediaArticle rdf:resource="http://oc.wikipedia.org/wiki/Ambrun"/>
  <gn:wikipediaArticle rdf:resource="http://pl.wikipedia.org/wiki/Embrun"/>
  <gn:wikipediaArticle rdf:resource="http://vo.wikipedia.org/wiki/Embrun_%28Hautes-Alpes%29"/>
</gn:Feature>
<foaf:Document rdf:about="http://sws.geonames.org/3020251/about.rdf">  - not used
  <foaf:primaryTopic rdf:about="http://sws.geonames.org/3020251/"/> - not used
  <cc:license rdf:resource="http://creativecommons.org/licenses/by/3.0/"/> - not used
  <cc:attributionURL rdf:resource="http://sws.geonames.org/3020251/"/> - not used
  <cc:attributionName rdf:datatype="http://www.w3.org/2001/XMLSchema#string">GeoNames</cc:attributionName> - not used
  <dcterms:created rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2006-01-15</dcterms:created> - not used
  <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2010-04-19</dcterms:modified> - not used
</foaf:Document> - not used
</rdf:RDF>

The EVENT vocabulary (http://motools.sourceforge.net/event/event.html) seems to tie these nicely together: use this first, 
but TIME instead of TIMELINE
