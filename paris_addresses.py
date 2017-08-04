#! /usr/bin/python3
# vim: set expandtab tabstop=4 shiftwidth=4 :
"""Useful addresses in Paris."""
from util_api import coord, get_coord_from_addr

if False:
    swimming_pools = {
        'Piscine René et André Mourlon':          get_coord_from_addr('19 Rue Gaston de Caillavet, Paris'),
        'Piscine Jean Taris':                     get_coord_from_addr('16 Rue Thouin, Paris'),
        'Piscine Pontoise':                       get_coord_from_addr('19 Rue de Pontoise, Paris'),
        'Piscine Keller':                         get_coord_from_addr('14 Rue de l\'Ingénieur Robert Keller, Paris'),
        'Piscine Jacqueline Auriol ex Beaujon':   get_coord_from_addr('7 Allée Louis de Funès, Paris'),
        'Piscine Georges Hermant':                get_coord_from_addr('8-10 Rue David d\'Angers, Paris'),
        'Piscine Château-Landon':                 get_coord_from_addr('31 Rue du Château Landon, Paris'),
        'Piscine Paul Valeyre':                   get_coord_from_addr('22 rue de Rochechouart, Paris'),
        'Piscine Catherine Lagatu ex Parmentier': get_coord_from_addr('155 avenue Parmentier, Paris'),
        'Piscine Georges Rigal':                  get_coord_from_addr('115 boulevard de Charonne, Paris'),
        'Piscine Blomet':                         get_coord_from_addr('17 rue Blomet, Paris'),
        'Piscine Henry de Montherlant':           get_coord_from_addr('30 boulevard Lannes, Paris'),
    }
else:
    swimming_pools = {
        'Piscine Jacqueline Auriol ex Beaujon': coord(address='7 Allée Louis de Funès, 75008 Paris-8E-Arrondissement, France', latitude=48.8762713, longitude=2.3065426),
        'Piscine René et André Mourlon': coord(address='19 Rue Gaston de Caillavet, 75015 Paris-15E-Arrondissement, France', latitude=48.8488991, longitude=2.2849313),
        'Piscine Keller': coord(address="14 Rue de l'Ingénieur Robert Keller, 75015 Paris, France", latitude=48.8473705, longitude=2.2820431),
        'Piscine Pontoise': coord(address='19 Rue de Pontoise, 75005 Paris-5E-Arrondissement, France', latitude=48.8492363, longitude=2.3515924),
        'Piscine Jean Taris': coord(address='16 Rue Thouin, 75005 Paris, France', latitude=48.8447257, longitude=2.3479414),
        'Piscine Georges Hermant': coord(address="10 Rue David d'Angers, 75019 Paris, France", latitude=48.8826541, longitude=2.3896377),
        'Piscine Château-Landon': coord(address='31 Rue du Château Landon, 75010 Paris, France', latitude=48.8833274, longitude=2.3632885),
        'Piscine Paul Valeyre': coord(address='22 Rue de Rochechouart, 75009 Paris, France', latitude=48.8779562, longitude=2.345001),
        'Piscine Georges Rigal': coord(address='115 Boulevard de Charonne, 75011 Paris, France', latitude=48.856438, longitude=2.393391),
        'Piscine Blomet': coord(address='17 Rue Blomet, 75015 Paris, France', latitude=48.8429844, longitude=2.3078971),
        'Piscine Catherine Lagatu ex Parmentier': coord(address='155 Avenue Parmentier, 75010 Paris, France', latitude=48.8715431, longitude=2.369443),
        'Piscine Henry de Montherlant': coord(address='30 Boulevard Lannes, 75116 Paris, France', latitude=48.8675411, longitude=2.271703),
    }
