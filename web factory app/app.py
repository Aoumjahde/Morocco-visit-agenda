from flask import Flask, render_template, request 
app = Flask(__name__)
activities = {
    "Outdoor Adventures": [ # category 01
        {
            "name": "Camel Trekking in the Sahara Desert",
            "location": "Merzouga",
            "description": "Explore the vast dunes of Erg Chebbi on camelback, experiencing the beauty of the desert and its golden sands.",
            "url": "https://www.visitmorocco.com/en/travel/sahara",
            "image": "https://wilddesertofmorocco.com/wp-content/uploads/2023/04/camel-caravan-late-afternoon-2-1290X540.jpg"
        },

        {
            "name": "Hiking in the High Atlas Mountains",
            "location": "Imlil, near Mount Toubkal",
            "description": "Discover breathtaking trails, traditional Berber villages, and stunning mountain landscapes.",
            "url": "https://www.trekkinginmorocco.com/",
            "image": "https://i.natgeofe.com/n/197fcc7b-4cc6-45ff-b79b-fb57eadb7436/Morocco_02_AZZADEN_VALLEY_0423_HR.jpg?w=1280&h=853"
        },

        {
            "name": "Surfing in Taghazout",
            "location": "Taghazout, near Agadir",
            "description": "Enjoy world-class surfing on Morocco's Atlantic coast with a laid-back beach town vibe.",
            "url": "https://www.surfmaroc.com/",
            "image": "https://thesurfatlas.com/wp-content/uploads/2020/09/Taghazout-surf-1.jpg"
        },

        {
            "name": "Hot Air Balloon Ride over Marrakech",
            "location": "Marrakech",
            "description": "Soar above the Red City and surrounding landscapes for an unforgettable sunrise experience.",
            "url": "https://www.ciel-marrakech.com/en/",
            "image": "https://media.tacdn.com/media/attractions-splice-spp-674x446/06/e8/e9/e5.jpg"
        },

        {
            "name": "Climbing in Todra Gorge",
            "location": "Tinghir",
            "description": "Challenge yourself with rock climbing or explore the dramatic canyon's hiking trails.",
            "url": "https://www.planetware.com/morocco/todra-gorge-mar-dr-sotg.htm",
            "image": "http://climbmorocco.com/wp-content/uploads/2012/03/Todra12-e1371625415614.jpg"
        },

        {
            "name": "Quad Biking in Agafay Desert",
            "location": "Agafay Desert, near Marrakech",
            "description": "Ride through rocky desert terrain and enjoy panoramic views of the Atlas Mountains.",
            "url": "https://www.getyourguide.com/marrakech-l208/agafay-desert-quad-biking-tour-t204420/",
            "image": "https://majatravels.com/wp-content/uploads/2023/04/climbing-todra-sport-scaled.jpg"
        },

        {
            "name": "Exploring the Blue Streets of Chefchaouen",
            "location": "Chefchaouen",
            "description": "Stroll through the picturesque blue-painted streets of this serene mountain town.",
            "url": "https://www.visitmorocco.com/en/travel/chefchaouen",
            "image": "https://www.traveltalktours.com/wp-content/uploads/2022/03/milad-alizadeh-JibMa0FbyHw-unsplash-1024x683.jpg"
        },

        {
            "name": "Windsurfing in Essaouira",
            "location": "Essaouira",
            "description": "Experience strong Atlantic winds perfect for windsurfing and kiteboarding in this charming coastal city.",
            "url": "https://www.essaouira.com/",
            "image": "https://www.sportif.travel/images/uploads/centres/Essaouira/WS/5_Morocco_Essaouira_Windsurf_Kitesurf_Holiday_Action_Kitesurf_Lesson_800x533.jpg"
        },

        {
            "name": "Horseback Riding in Souss Massa National Park",
            "location": "Souss Massa National Park, near Agadir",
            "description": "Ride through coastal dunes and spot unique wildlife, including gazelles and flamingos.",
            "url": "https://www.visitmorocco.com/en/travel/souss-massa-national-park",
            "image": "https://www.stunningtravel.nl/wp-content/uploads/2021/02/Souss-Massa-National-Park-696x463.jpg"
        },

        {
            "name": "Caving at Friouato Caves",
            "location": "Taza",
            "description": "Descend into Morocco's largest cave system and explore its fascinating geological formations.",
            "url": "https://www.moroccoworldnews.com/2020/12/328366/friouato-caves-taza-a-hidden-natural-wonder-in-morocco/",
            "image": "https://1.bp.blogspot.com/-di5wg06hXIU/Xcm0cZWrb-I/AAAAAAAAGoU/p2Y1mqdEK7UDqvdqqFo5QeOt0q3nwz5igCLcBGAsYHQ/s1600/frou.PNG"
        }
    ],
    #************************************
    "Historical Sites": [ # category 02
        {
            "name": "Hassan II Mosque",
            "location": "Casablanca",
            "description": "The largest mosque in Morocco, renowned for its stunning architecture and seaside location.",
            "url": "https://en.wikipedia.org/wiki/Hassan_II_Mosque",
            "image": "https://images.memphistours.com/large/d4582f9dbf053d1c4238918d4932b6a1.jpg"
        },

        {
            "name": "Volubilis",
            "location": "Near Meknes",
            "description": "A well-preserved Roman city and UNESCO World Heritage site, featuring stunning mosaics and ruins.",
            "url": "https://en.wikipedia.org/wiki/Volubilis",
            "image": "https://i.pinimg.com/originals/6a/d4/59/6ad4596310cd0b59cebf11f85b474b4b.jpg"
        },

        {
            "name": "Aït Benhaddou",
            "location": "Ouarzazate",
            "description": "A fortified village and UNESCO site, famous for its earthen buildings and appearances in movies like 'Gladiator.'",
            "url": "https://en.wikipedia.org/wiki/A%C3%AFt_Benhaddou",
            "image": "https://ucarecdn.com/a8b1b6cb-45cb-4b58-b596-82b1214f5063/"
        },

        {
            "name": "El Badi Palace",
            "location": "Marrakech",
            "description": "Ruins of a once-grand palace showcasing Saadian Dynasty architecture and history.",
            "url": "https://en.wikipedia.org/wiki/El_Badi_Palace",
            "image": "https://www.gpsmycity.com/img/gd_attr/19223.jpg"
        },

        {
            "name": "Saadian Tombs",
            "location": "Marrakech",
            "description": "A hidden necropolis dating back to the Saadian Dynasty, famous for its intricate decoration.",
            "url": "https://saadiantombs.com/",
            "image": "https://global-geography.org/attach/Geography/Africa/Morocco/Pictures/Imperial_Cities/Rabat_-_Mausoleum_of_Mohammed_V_4/MA290_Mausoleum_Mohammed_V.jpg"
        },

        {
            "name": "Chellah",
            "location": "Rabat",
            "description": "An ancient necropolis and Roman ruin located in the capital city of Morocco.",
            "url": "https://en.wikipedia.org/wiki/Chellah",
            "image": "https://media-cdn.sygictraveldata.com/media/800x600/612664395a40232133447d33247d383738373936"
        },

        {
            "name": "Bahia Palace",
            "location": "Marrakech",
            "description": "A 19th-century palace showcasing stunning Moroccan architecture and lush gardens.",
            "url": "https://bahia-palace.com/",
            "image": "https://morocco-phototours.com/wp-content/uploads/2023/07/Bahia-Palace.jpg"
        },

        {
            "name": "Kasbah of the Udayas",
            "location": "Rabat",
            "description": "A historic kasbah with picturesque streets, Andalusian gardens, and ocean views.",
            "url": "https://thinkmorocco.com/kasbah-of-udayas/",
            "image": "https://images.memphistours.com/large/75e0e0cbb7e76afe2e054d091912bb41.jpg"
        },
        {
            "name": "Fez Medina (Fes el Bali)",
            "location": "Fez",
            "description": "One of the oldest and largest medieval cities in the world, and a UNESCO World Heritage site.",
            "url": "https://www.fes.fr/medina-fes-el-bali",
            "image": "https://teaspoonofadventure.com/wp-content/uploads/2020/05/IMG_1613-760x1013.jpg"
        },

        {
            "name": "Mausoleum of Mohammed V",
            "location": "Rabat",
            "description": "The tomb of King Mohammed V, featuring intricate Moroccan artistry and history.",
            "url": "https://thinkmorocco.com/mohamed-v-mausoleum/",
            "image": "https://www.gpsmycity.com/img/gd_attr/44615.jpg"
        }

    ],
    #************************************
    "Villages": [ # category 04
        {
            "name": "Chefchaouen (The Blue Pearl)",
            "location": "Rif Mountains",
            "description": "Known for its blue-washed buildings and relaxed atmosphere, Chefchaouen is one of the most picturesque villages in Morocco.",
            "url": "https://en.wikipedia.org/wiki/Chefchaouen",
            "image": "https://www.solosophie.com/wp-content/uploads/2023/02/Chefchaouen_1860127240-960x629.jpeg"},

        {
            "name": "Imlil",
            "location": "High Atlas Mountains",
            "description": "A tranquil mountain village and gateway to Toubkal National Park, perfect for hikers and nature lovers.",
            "url": "https://en.wikipedia.org/wiki/Imlil,_Morocco",
            "image": "https://marrakech-riads.com/wp-content/uploads/2018/09/imlil-marrakech-riads.jpg"},

        {
            "name": "Aït Benhaddou",
            "location": "Ouarzazate Region",
            "description": "A historic fortified village and UNESCO World Heritage site, famous for its kasbahs and movie appearances.",
            "url": "https://en.wikipedia.org/wiki/A%C3%AFt_Benhaddou",
            "image": "https://www.airpano.com/photogallery/images_1550/195_429576.jpg"},

        {
            "name": "Asilah",
            "location": "Atlantic Coast",
            "description": "A charming coastal village known for its whitewashed medina, vibrant murals, and seaside views.",
            "url": "https://en.wikipedia.org/wiki/Asilah",
            "image": "https://www.traveloffpath.com/wp-content/uploads/2019/06/Asilah-Morocco.jpg"},

        {
            "name": "Moulay Idriss Zerhoun",
            "location": "Near Meknes",
            "description": "A sacred village named after the founder of Morocco’s first dynasty, with stunning views and a peaceful vibe.",
            "url": "https://en.wikipedia.org/wiki/Moulay_Idriss_Zerhoun",
            "image": "https://heroesofadventure.com/wp-content/uploads/2018/08/Moulay_Idriss_2.jpg"},

        {
            "name": "Tafraoute",
            "location": "Anti-Atlas Mountains",
            "description": "A colorful village surrounded by unique pink granite formations and palm groves.",
            "url": "https://en.wikipedia.org/wiki/Tafraout",
            "image": "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/morocco-south-morocco-blue-rocks-near-tafraoute-painted-by-belgian-artist-jean-veran-ugo-mellone.jpg"},

        {
            "name": "Merzouga",
            "location": "Sahara Desert",
            "description": "A small desert village near the Erg Chebbi dunes, offering camel treks and stunning sunrises.",
            "url": "https://en.wikipedia.org/wiki/Merzouga",
            "image": "https://media.hostunusual.com/wp-content/uploads/2022/04/31201356/merzouga-luxury-tented-camp-Main-ext-1024x683.jpg"},

        {
            "name": "Ouirgane",
            "location": "High Atlas Mountains",
            "description": "A serene mountain village surrounded by olive groves and a great base for exploring nature trails.",
            "url": "https://www.lonelyplanet.com/morocco/ouirgane",
            "image": "https://www.souladventuremorocco.com/wp-content/uploads/2019/09/Ouirgane-Valley-Lake-Ouirgane-Marrakech-excursion.jpg"},

        {
            "name": "Tamnougalt",
            "location": "Draa Valley",
            "description": "An ancient kasbah village with earthen architecture, palm groves, and a rich history.",
            "url": "https://en.wikipedia.org/wiki/Tamnougalt",
            "image": "https://www.traveltamegroute.net/wp-content/uploads/2017/03/Fotolia_140664315_Subscription_Monthly_M.jpg"},

        {
            "name": "Imsouane",
            "location": "Atlantic Coast",
            "description": "A tranquil fishing village popular among surfers and seafood lovers, with stunning beaches and views.",
            "url": "https://www.bestsurfdestinations.com/surfing-imsouane/",
            "image": "https://www.travelsurfmorocco.com/wp-content/uploads/2016/04/1-imessouane-bay.jpg"}
    ],
    "Food & Drink": [ 
        {
            "name": "Tagine Cooking Experience",
            "location": "Marrakech",
            "description": "Learn to prepare Morocco’s iconic slow-cooked dish, rich in spices and flavors, in a traditional tagine pot.",
            "url": "https://en.wikipedia.org/wiki/Tajine",
            "image": "https://simplynaturalgourmet.com/wp-content/uploads/2014/07/tandoori-chicken-tagine4.jpg"
        },
        {
            "name": "Moroccan Mint Tea Ceremony",
            "location": "Fez",
            "description": "Experience the art of pouring and drinking traditional mint tea, a symbol of hospitality in Morocco.",
            "url": "https://en.wikipedia.org/wiki/Maghrebi_mint_tea",
            "image": "https://moroccanfoodtour.com/wp-content/uploads/2020/07/moroccan-food-tour-Moroccan-mint-tea-915x610.jpg"
        },
        {
            "name": "Djemaa el-Fna Food Stalls",
            "location": "Marrakech",
            "description": "Sample a variety of Moroccan street food in the bustling main square, from grilled meats to pastries.",
            "url": "https://www.tripadvisor.com/ShowTopic-g293734-i9196-k13667197-Which_street_food_stalls_to_try_in_Jemaa_El_Fna-Marrakech_Marrakech_Safi.html",
            "image": "https://res.cloudinary.com/lastminute-contenthub/s--Wo1hXr2p--/c_limit,h_999999,w_1024/f_auto/q_auto:eco/v1/Hub-Live/LastminuteFR/blog/images/e39f7f33-3e5f-4841-870a-bcb32ab67662"
        },
        {
            "name": "Harira Soup Tasting",
            "location": "Casablanca",
            "description": "Try Morocco’s traditional soup, made with lentils, chickpeas, and spices, often served during Ramadan.",
            "url": "https://ilvasodipandoro.com/fr/la-harira-marocaine/",
            "image": "https://tasteofmaroc.com/wp-content/uploads/2017/05/harira-2-moroccan-soup-picturepartners-bigstock-740x493.jpg.webp"
        },
        {
            "name": "Couscous Fridays",
            "location": "Rabat",
            "description": "Enjoy authentic couscous, a staple dish traditionally served on Fridays, made with fluffy grains and vegetables.",
            "url": "https://tasteofmaroc.com/moroccan-couscous-with-seven-vegetables/",
            "image": "https://spicebreeze.com/wp-content/uploads/2018/10/couscous.jpg"
        },
        {
            "name": "Seafood at Agadir Marina",
            "location": "Agadir",
            "description": "Savor fresh seafood at waterfront restaurants, from grilled fish to fried calamari.",
            "url": "https://www.tripadvisor.com/Restaurant_Review-g293731-d6697377-Reviews-Pure_Passion_Restaurant-Agadir_Souss_Massa.html",
            "image": "https://www.barcelo.com/guia-turismo/wp-content/uploads/2024/09/ok-comer-en-agadir.jpg"
        },
        {
            "name": "Pastilla Feast",
            "location": "Fez",
            "description": "Taste this sweet and savory pastry filled with spiced chicken or pigeon, almonds, and cinnamon.",
            "url": "https://www.196flavors.com/pastilla/",
            "image": "https://www.196flavors.com/wp-content/uploads/2016/11/pastilla-9.jpg"
        },
        {
            "name": "Visit an Argan Oil Cooperative",
            "location": "Essaouira",
            "description": "Learn about and taste argan oil, a versatile Moroccan product used for cooking and cosmetics.",
            "url": "https://thetravelbunny.com/tighanimine-womens-fairtrade-argan-oil-cooperative/",
            "image": "https://www.culturecherifienne.com/wp-content/uploads/2018/04/coop%C3%A9rative-arganier-femmes.jpg"
        },
        {
            "name": "Moroccan Pastries Tasting",
            "location": "Meknes",
            "description": "Sample traditional sweets like *chebakia* (fried sesame cookies) and *ghriba* (almond biscuits).",
            "url": "https://www.chefspencil.com/moroccan-desserts/",
            "image": "https://primemoroccotours.com/wp-content/uploads/2022/07/Moroccan-Sweets-12.jpg"
        },
        {
            "name": "Visit a Traditional Riad for Dinner",
            "location": "Chefchaouen",
            "description": "Enjoy a multi-course Moroccan meal in the courtyard of a traditional riad, surrounded by beautiful décor.",
            "url": "https://travelcollecting.com/best-riads-in-marrakech/",
            "image": "https://images.lifestyleasia.com/wp-content/uploads/2019/01/28174044/riad-hero-2.jpg?tr=w-1366"
        }
]

    }


@app.route('/')
def home():
    return render_template('home.html',  categories=activities.keys())


@app.route('/activities', methods = ['POST'])
def showing_activities():
    category = request.form.get('category')
    choes_an_activitie = activities.get(category, [])
    
    return render_template('activities.html', category= category, activities = choes_an_activitie)


if __name__ == '__main__':
    app.run(debug=True)