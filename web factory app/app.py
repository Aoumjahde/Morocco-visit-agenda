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
            "url": "https://www.theculturetrip.com/africa/morocco/articles/a-guide-to-the-hassan-ii-mosque-in-casablanca",
            "image": "https://images.memphistours.com/large/d4582f9dbf053d1c4238918d4932b6a1.jpg"
        },

        {
            "name": "Volubilis",
            "location": "Near Meknes",
            "description": "A well-preserved Roman city and UNESCO World Heritage site, featuring stunning mosaics and ruins.",
            "url": "https://www.planetware.com/tourist-attractions/morocco-meknes-volubilis-mar-mek.htm",
            "image": "https://i.pinimg.com/originals/6a/d4/59/6ad4596310cd0b59cebf11f85b474b4b.jpg"
        },

        {
            "name": "Aït Benhaddou",
            "location": "Ouarzazate",
            "description": "A fortified village and UNESCO site, famous for its earthen buildings and appearances in movies like 'Gladiator.'",
            "url": "https://www.moroccotours.net/blog/ait-benhaddou-morocco",
            "image": "https://ucarecdn.com/a8b1b6cb-45cb-4b58-b596-82b1214f5063/"
        },

        {
            "name": "El Badi Palace",
            "location": "Marrakech",
            "description": "Ruins of a once-grand palace showcasing Saadian Dynasty architecture and history.",
            "url": "https://www.roughguides.com/morocco/marrakech/el-badi-palace/",
            "image": "https://www.gpsmycity.com/img/gd_attr/19223.jpg"
        },

        {
            "name": "Saadian Tombs",
            "location": "Marrakech",
            "description": "A hidden necropolis dating back to the Saadian Dynasty, famous for its intricate decoration.",
            "url": "https://www.traveltriangle.com/blog/saadian-tombs-marrakech/",
            "image": "https://global-geography.org/attach/Geography/Africa/Morocco/Pictures/Imperial_Cities/Rabat_-_Mausoleum_of_Mohammed_V_4/MA290_Mausoleum_Mohammed_V.jpg"
        },

        {
            "name": "Chellah",
            "location": "Rabat",
            "description": "An ancient necropolis and Roman ruin located in the capital city of Morocco.",
            "url": "https://www.moroccotravelblog.com/chellah-the-roots-of-rabat/",
            "image": "https://media-cdn.sygictraveldata.com/media/800x600/612664395a40232133447d33247d383738373936"
        },

        {
            "name": "Bahia Palace",
            "location": "Marrakech",
            "description": "A 19th-century palace showcasing stunning Moroccan architecture and lush gardens.",
            "url": "https://www.tripadvisor.com/Attraction_Review-g293734-d318068-Reviews-Bahia_Palace-Marrakech_Marrakech_Safi.html",
            "image": "https://morocco-phototours.com/wp-content/uploads/2023/07/Bahia-Palace.jpg"
        },

        {
            "name": "Kasbah of the Udayas",
            "location": "Rabat",
            "description": "A historic kasbah with picturesque streets, Andalusian gardens, and ocean views.",
            "url": "https://www.touropia.com/kasbah-of-the-udayas/",
            "image": "https://images.memphistours.com/large/75e0e0cbb7e76afe2e054d091912bb41.jpg"
        },
        {
            "name": "Fez Medina (Fes el Bali)",
            "location": "Fez",
            "description": "One of the oldest and largest medieval cities in the world, and a UNESCO World Heritage site.",
            "url": "https://www.planetware.com/morocco/fez-el-bali-fes-mar-fes.htm",
            "image": "https://teaspoonofadventure.com/wp-content/uploads/2020/05/IMG_1613-760x1013.jpg"
        },

        {
            "name": "Mausoleum of Mohammed V",
            "location": "Rabat",
            "description": "The tomb of King Mohammed V, featuring intricate Moroccan artistry and history.",
            "url": "https://www.moroccoworldnews.com/2021/01/334824/mausoleum-of-mohammed-v-in-rabat-morocco",
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
            "image": "https://www.pexels.com/photo/a-narrow-hallway-4652060/"},

        {
            "name": "Imlil",
            "location": "High Atlas Mountains",
            "description": "A tranquil mountain village and gateway to Toubkal National Park, perfect for hikers and nature lovers.",
            "url": "https://en.wikipedia.org/wiki/Imlil,_Morocco",
            "image": "https://www.bing.com/images/search?q=imlil%2c+marrakesh-safi&cbn=KnowledgeCard&stid=4b5999ce-96b2-5832-7889-3631538f545b&thid=OSK.HEROPFaQlvo0CBYqg3EnRfWiPyIYD590vcNbFsZxzgMQ1T0Y&FORM=KCHIMM"},

        {
            "name": "Aït Benhaddou",
            "location": "Ouarzazate Region",
            "description": "A historic fortified village and UNESCO World Heritage site, famous for its kasbahs and movie appearances.",
            "url": "https://en.wikipedia.org/wiki/A%C3%AFt_Benhaddou",
            "image": "https://www.bing.com/images/search?q=A%c3%aft+Benhaddou&id=6BB3AA9A4F80918D418974256B7848CB1C16F02A"},

        {
            "name": "Asilah",
            "location": "Atlantic Coast",
            "description": "A charming coastal village known for its whitewashed medina, vibrant murals, and seaside views.",
            "url": "https://en.wikipedia.org/wiki/Asilah",
            "image": "https://www.bing.com/images/search?q=asilah&cbn=KnowledgeCard&stid=2a8869e8-24b7-2922-3070-2f0075a79a65&thid=OSK.HEROP9S5rqWwPV4gOCdC9HM-aX5RxUNORv7AARc3roKy5g0I&FORM=KCHIMM"},

        {
            "name": "Moulay Idriss Zerhoun",
            "location": "Near Meknes",
            "description": "A sacred village named after the founder of Morocco’s first dynasty, with stunning views and a peaceful vibe.",
            "url": "https://en.wikipedia.org/wiki/Moulay_Idriss_Zerhoun",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=Wb0oM6tc&id=7EFDAB73CD7FA76406C630E56404CD35FCD7F4BB&thid=OIP.Wb0oM6tcJkTw1_OxAI_-QgHaFO&mediaurl=https%3a%2f%2fheroesofadventure.com%2fwp-content%2fuploads%2f2018%2f08%2fMoulay_Idriss_2.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.59bd2833ab5c2644f0d7f3b1008ffe42%3frik%3du%252fTX%252fDXNBGTlMA%26pid%3dImgRaw%26r%3d0&exph=1342&expw=1900&q=Moulay+Idriss+Zerhoun&simid=607991297889031834&FORM=IRPRST&ck=D64D54701F044DC994A1F1D11313188B&selectedIndex=1&itb=0"},

        {
            "name": "Tafraoute",
            "location": "Anti-Atlas Mountains",
            "description": "A colorful village surrounded by unique pink granite formations and palm groves.",
            "url": "https://en.wikipedia.org/wiki/Tafraout",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=3nPtT%2fTh&id=8DA392B65B052A29C166477B607865BD3C565C40&thid=OIP.3nPtT_ThJpSSYxhcrl5UEwHaE6&mediaurl=https%3a%2f%2fwww.moroccoprivatetours.net%2fuploads%2f346_tafraoute1.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.de73ed4ff4e126949263185cae5e5413%3frik%3dQFxWPL1leGB7Rw%26pid%3dImgRaw%26r%3d0&exph=680&expw=1024&q=Tafraoute&simid=608005037435793921&FORM=IRPRST&ck=C31555BB99426C5433895309D198718E&selectedIndex=2&itb=0"},

        {
            "name": "Merzouga",
            "location": "Sahara Desert",
            "description": "A small desert village near the Erg Chebbi dunes, offering camel treks and stunning sunrises.",
            "url": "https://en.wikipedia.org/wiki/Merzouga",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=ztFhmjIl&id=6FB3787E8C1817C9709E4863A1CEDB243B882706&thid=OIP.ztFhmjIla_sDaJdNSDoLXAHaEK&mediaurl=https%3a%2f%2fcdn.getyourguide.com%2fimg%2flocation%2f5ce408a48feba.jpeg%2f88.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.ced1619a32256bfb0368974d483a0b5c%3frik%3dBieIOyTbzqFjSA%26pid%3dImgRaw%26r%3d0&exph=1350&expw=2400&q=Merzouga&simid=608001356672747759&FORM=IRPRST&ck=31E0E0C6211234EBC3EA50D3B721DF21&selectedIndex=0&itb=0"},

        {
            "name": "Ouirgane",
            "location": "High Atlas Mountains",
            "description": "A serene mountain village surrounded by olive groves and a great base for exploring nature trails.",
            "url": "https://www.lonelyplanet.com/morocco/ouirgane",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=Xg%2fuL0Md&id=FC340A6DB3C6BDA9DBDC082E913892584181EF00&thid=OIP.Xg_uL0Md1_ez3WucO7UupQHaEo&mediaurl=https%3a%2f%2fwww.souladventuremorocco.com%2fwp-content%2fuploads%2f2019%2f09%2fOuirgane-Valley-Lake-Ouirgane-Marrakech-excursion.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.5e0fee2f431dd7f7b3dd6b9c3bb52ea5%3frik%3dAO%252bBQViSOJEuCA%26pid%3dImgRaw%26r%3d0%26sres%3d1%26sresct%3d1%26srh%3d800%26srw%3d1280&exph=500&expw=800&q=Ouirgane&simid=607996357336514657&FORM=IRPRST&ck=7E978044CD38F4910E66FF00EB850EFD&selectedIndex=1&itb=0"},

        {
            "name": "Tamnougalt",
            "location": "Draa Valley",
            "description": "An ancient kasbah village with earthen architecture, palm groves, and a rich history.",
            "url": "https://en.wikipedia.org/wiki/Tamnougalt",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=nxA916ta&id=C59CBE7C8394AFF68345D5DAEF517221480279C5&thid=OIP.nxA916taqNypWV8ATfyfRgHaE8&mediaurl=https%3a%2f%2fwww.thisfabtrek.com%2fjourney%2fafrica%2fmorocco%2f20050323-tamnougalt%2ftamn-kasbah2-4.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.9f103dd7ab5aa8dca9595f004dfc9f46%3frik%3dxXkCSCFyUe%252fa1Q%26pid%3dImgRaw%26r%3d0&exph=1024&expw=1536&q=Tamnougalt&simid=608018012556575053&FORM=IRPRST&ck=98D20955B24E524A42DA5C1008EF5760&selectedIndex=8&itb=0"},

        {
            "name": "Imsouane",
            "location": "Atlantic Coast",
            "description": "A tranquil fishing village popular among surfers and seafood lovers, with stunning beaches and views.",
            "url": "https://www.surfertoday.com/travel/imsouane",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=CS7RNAEd&id=63D54C45E067EEDB0C37980EF32F5786AA6FEFE6&thid=OIP.CS7RNAEd32zRduMWzeDG2QHaE8&mediaurl=https%3a%2f%2fwww.zensurfmorocco.com%2fwp-content%2fuploads%2f2023%2f06%2fCHU6101-S-1.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.092ed134011ddf6cd176e316cde0c6d9%3frik%3d5u9vqoZXL%252fMOmA%26pid%3dImgRaw%26r%3d0&exph=801&expw=1200&q=Imsouane&simid=608026516584995729&FORM=IRPRST&ck=534EA65E8DECE4D6545B59F059C8BE08&selectedIndex=0&itb=0"}
    ],
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