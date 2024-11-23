from flask import Flask, render_template, request 
app = Flask(__name__)
activities = {
"Outdoor Adventures": [ # category 01
    {
        "name": "Camel Trekking in the Sahara Desert",
        "location": "Merzouga",
        "description": "Explore the vast dunes of Erg Chebbi on camelback, experiencing the beauty of the desert and its golden sands.",
        "url": "https://www.visitmorocco.com/en/travel/sahara",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/48/Sahara_Desert_Camel_Ride.jpg"},

    {
        "name": "Hiking in the High Atlas Mountains",
        "location": "Imlil, near Mount Toubkal",
        "description": "Discover breathtaking trails, traditional Berber villages, and stunning mountain landscapes.",
        "url": "https://www.trekkinginmorocco.com/",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Imlil%2C_Morocco.jpg"},
    
    {
        "name": "Surfing in Taghazout",
        "location": "Taghazout, near Agadir",
        "description": "Enjoy world-class surfing on Morocco's Atlantic coast with a laid-back beach town vibe.",
        "url": "https://www.surfmaroc.com/",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Taghazout.jpg"},

    {
        "name": "Hot Air Balloon Ride over Marrakech",
        "location": "Marrakech",
        "description": "Soar above the Red City and surrounding landscapes for an unforgettable sunrise experience.",
        "url": "https://www.ciel-marrakech.com/en/",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/99/Marrakech_Balloon.jpg"},

    {
        "name": "Climbing in Todra Gorge",
        "location": "Tinghir",
        "description": "Challenge yourself with rock climbing or explore the dramatic canyon's hiking trails.",
        "url": "https://www.planetware.com/morocco/todra-gorge-mar-dr-sotg.htm",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/81/Todra_Gorge.jpg"},

    {
        "name": "Quad Biking in Agafay Desert",
        "location": "Agafay Desert, near Marrakech",
        "description": "Ride through rocky desert terrain and enjoy panoramic views of the Atlas Mountains.",
        "url": "https://www.getyourguide.com/marrakech-l208/agafay-desert-quad-biking-tour-t204420/",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/69/Agafay_Desert.jpg"},

    {
        "name": "Exploring the Blue Streets of Chefchaouen",
        "location": "Chefchaouen",
        "description": "Stroll through the picturesque blue-painted streets of this serene mountain town.",
        "url": "https://www.visitmorocco.com/en/travel/chefchaouen",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Chefchaouen-Street.jpg"},

    {
        "name": "Windsurfing in Essaouira",
        "location": "Essaouira",
        "description": "Experience strong Atlantic winds perfect for windsurfing and kiteboarding in this charming coastal city.",
        "url": "https://www.essaouira.com/",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/94/Essaouira_Beach.jpg"},

    {
        "name": "Horseback Riding in Souss Massa National Park",
        "location": "Souss Massa National Park, near Agadir",
        "description": "Ride through coastal dunes and spot unique wildlife, including gazelles and flamingos.",
        "url": "https://www.visitmorocco.com/en/travel/souss-massa-national-park",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Souss_Massa_Park.jpg"},
        
    {
        "name": "Caving at Friouato Caves",
        "location": "Taza",
        "description": "Descend into Morocco's largest cave system and explore its fascinating geological formations.",
        "url": "https://www.moroccoworldnews.com/2020/12/328366/friouato-caves-taza-a-hidden-natural-wonder-in-morocco/",
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Friouato_Cave.jpg"
        }
    ],
    #************************************
    "Historical Sites": [ # category 02
        {
            "name": "Hassan II Mosque",
            "location": "Casablanca",
            "description": "The largest mosque in Morocco, renowned for its stunning architecture and seaside location.",
            "url": "https://en.wikipedia.org/wiki/Hassan_II_Mosque",
            "image": "https://upload.wikimedia.org/wikipedia/commons/3/32/Mosquee_Hassan_II.jpg"},

        {
            "name": "Volubilis",
            "location": "Near Meknes",
            "description": "A well-preserved Roman city and UNESCO World Heritage site, featuring stunning mosaics and ruins.",
            "url": "https://en.wikipedia.org/wiki/Volubilis",
            "image": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Volubilis_Morocco_panorama.jpg"},

        {
            "name": "Aït Benhaddou",
            "location": "Ouarzazate",
            "description": "A fortified village and UNESCO site, famous for its earthen buildings and appearances in movies like 'Gladiator.'",
            "url": "https://en.wikipedia.org/wiki/A%C3%AFt_Benhaddou",
            "image": "https://upload.wikimedia.org/wikipedia/commons/2/28/A%C3%AFt_Benhaddou.jpg"},

        {
            "name": "El Badi Palace",
            "location": "Marrakech",
            "description": "Ruins of a once-grand palace showcasing Saadian Dynasty architecture and history.",
            "url": "https://en.wikipedia.org/wiki/El_Badi_Palace",
            "image": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Palais_El_Badi.jpg"},

        {
            "name": "Saadian Tombs",
            "location": "Marrakech",
            "description": "A hidden necropolis dating back to the Saadian Dynasty, famous for its intricate decoration.",
            "url": "https://en.wikipedia.org/wiki/Saadian_Tombs",
            "image": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Saadian_tombs_interior.jpg"},

        {
            "name": "Chellah",
            "location": "Rabat",
            "description": "An ancient necropolis and Roman ruin located in the capital city of Morocco.",
            "url": "https://en.wikipedia.org/wiki/Chellah",
            "image": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Chellah_ruins%2C_Rabat.jpg"},

        {
            "name": "Bahia Palace",
            "location": "Marrakech",
            "description": "A 19th-century palace showcasing stunning Moroccan architecture and lush gardens.",
            "url": "https://en.wikipedia.org/wiki/Bahia_Palace",
            "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Palais_de_la_Bahia%2C_Marrakech.jpg"},

        {
            "name": "Kasbah of the Udayas",
            "location": "Rabat",
            "description": "A historic kasbah with picturesque streets, Andalusian gardens, and ocean views.",
            "url": "https://en.wikipedia.org/wiki/Kasbah_of_the_Udayas",
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/48/Oudaia_Gate_in_Rabat.jpg"},

        {
            "name": "Fez Medina (Fes el Bali)",
            "location": "Fez",
            "description": "One of the oldest and largest medieval cities in the world, and a UNESCO World Heritage site.",
            "url": "https://en.wikipedia.org/wiki/Fes_el_Bali",
            "image": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Fes_Medina.jpg"},

        {
            "name": "Mausoleum of Mohammed V",
            "location": "Rabat",
            "description": "The tomb of King Mohammed V, featuring intricate Moroccan artistry and history.",
            "url": "https://en.wikipedia.org/wiki/Mausoleum_of_Mohammed_V",
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Mausol%C3%A9e_Mohammed_V_Rabat.jpg"
        }
    ],
    #************************************
    "Food & Drink": [ # category 03
        {
            "name": "Tagine Cooking Experience",
            "location": "Marrakech",
            "description": "Learn to prepare Morocco’s iconic slow-cooked dish, rich in spices and flavors, in a traditional tagine pot.",
            "url": "https://www.cookingclassmaroc.com",
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/43/Tajine_d%27agneau_aux_pruneaux.jpg" },
        {
            "name": "Moroccan Mint Tea Ceremony",
            "location": "Fez",
            "description": "Experience the art of pouring and drinking traditional mint tea, a symbol of hospitality in Morocco.",
            "url": "https://en.wikipedia.org/wiki/Maghrebi_mint_tea",
            "image": "https://upload.wikimedia.org/wikipedia/commons/2/27/Atay.jpg"},
            
        {
            "name": "Djemaa el-Fna Food Stalls",
            "location": "Marrakech",
            "description": "Sample a variety of Moroccan street food in the bustling main square, from grilled meats to pastries.",
            "url": "https://www.visitmorocco.com/en/marrakech",
            "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Djemaa_el_Fna_Marrakech.jpg"
        },
        {
            "name": "Harira Soup Tasting",
            "location": "Casablanca",
            "description": "Try Morocco’s traditional soup, made with lentils, chickpeas, and spices, often served during Ramadan.",
            "url": "https://www.marocmama.com/moroccan-harira-soup-recipe/",
            "image": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Harira_Maroc.jpg"},

        {
            "name": "Couscous Fridays",
            "location": "Rabat",
            "description": "Enjoy authentic couscous, a staple dish traditionally served on Fridays, made with fluffy grains and vegetables.",
            "url": "https://en.wikipedia.org/wiki/Couscous",
            "image": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Moroccan_couscous.jpg"},

        {
            "name": "Seafood at Agadir Marina",
            "location": "Agadir",
            "description": "Savor fresh seafood at waterfront restaurants, from grilled fish to fried calamari.",
            "url": "https://www.tripadvisor.com/Restaurants-g293731-c33-Agadir_Souss_Massa.html",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/82/Fish_meal_in_Agadir_Morocco.jpg"},

        {
            "name": "Pastilla Feast",
            "location": "Fez",
            "description": "Taste this sweet and savory pastry filled with spiced chicken or pigeon, almonds, and cinnamon.",
            "url": "https://en.wikipedia.org/wiki/Bastilla",
            "image": "https://upload.wikimedia.org/wikipedia/commons/2/28/Bastilla.jpg"},

        {
            "name": "Visit an Argan Oil Cooperative",
            "location": "Essaouira",
            "description": "Learn about and taste argan oil, a versatile Moroccan product used for cooking and cosmetics.",
            "url": "https://www.lonelyplanet.com/articles/moroccan-argan-oil",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/81/Argan_fruit_harvested.jpg"},

        {
            "name": "Moroccan Pastries Tasting",
            "location": "Meknes",
            "description": "Sample traditional sweets like *chebakia* (fried sesame cookies) and *ghriba* (almond biscuits).",
            "url": "https://tasteatlas.com/moroccan-desserts",
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/47/Moroccan_chebakia.jpg"},

        {
            "name": "Visit a Traditional Riad for Dinner",
            "location": "Chefchaouen",
            "description": "Enjoy a multi-course Moroccan meal in the courtyard of a traditional riad, surrounded by beautiful décor.",
            "url": "https://www.riadchefchaouen.com",
            "image": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Chefchaouen_mountain_view.jpg"}
    ],
    #************************************
    "Villages": [ # category 04
        {
            "name": "Chefchaouen (The Blue Pearl)",
            "location": "Rif Mountains",
            "description": "Known for its blue-washed buildings and relaxed atmosphere, Chefchaouen is one of the most picturesque villages in Morocco.",
            "url": "https://en.wikipedia.org/wiki/Chefchaouen",
            "image": "https://upload.wikimedia.org/wikipedia/commons/3/34/Chefchaouen_blue_street.jpg"},

        {
            "name": "Imlil",
            "location": "High Atlas Mountains",
            "description": "A tranquil mountain village and gateway to Toubkal National Park, perfect for hikers and nature lovers.",
            "url": "https://en.wikipedia.org/wiki/Imlil,_Morocco",
            "image": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Imlil.JPG"},

        {
            "name": "Aït Benhaddou",
            "location": "Ouarzazate Region",
            "description": "A historic fortified village and UNESCO World Heritage site, famous for its kasbahs and movie appearances.",
            "url": "https://en.wikipedia.org/wiki/A%C3%AFt_Benhaddou",
            "image": "https://upload.wikimedia.org/wikipedia/commons/2/28/A%C3%AFt_Benhaddou.jpg"},

        {
            "name": "Asilah",
            "location": "Atlantic Coast",
            "description": "A charming coastal village known for its whitewashed medina, vibrant murals, and seaside views.",
            "url": "https://en.wikipedia.org/wiki/Asilah",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/87/Asilah_medina_street.jpg"},

        {
            "name": "Moulay Idriss Zerhoun",
            "location": "Near Meknes",
            "description": "A sacred village named after the founder of Morocco’s first dynasty, with stunning views and a peaceful vibe.",
            "url": "https://en.wikipedia.org/wiki/Moulay_Idriss_Zerhoun",
            "image": "https://upload.wikimedia.org/wikipedia/commons/a/aa/Moulay_Idriss_%28Morocco%29.JPG"},

        {
            "name": "Tafraoute",
            "location": "Anti-Atlas Mountains",
            "description": "A colorful village surrounded by unique pink granite formations and palm groves.",
            "url": "https://en.wikipedia.org/wiki/Tafraout",
            "image": "https://upload.wikimedia.org/wikipedia/commons/5/59/Tafraoute_village.jpg"},

        {
            "name": "Merzouga",
            "location": "Sahara Desert",
            "description": "A small desert village near the Erg Chebbi dunes, offering camel treks and stunning sunrises.",
            "url": "https://en.wikipedia.org/wiki/Merzouga",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/81/Erg_Chebbi_dunes.jpg"},

        {
            "name": "Ouirgane",
            "location": "High Atlas Mountains",
            "description": "A serene mountain village surrounded by olive groves and a great base for exploring nature trails.",
            "url": "https://www.lonelyplanet.com/morocco/ouirgane",
            "image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Ouirgane.jpg"},

        {
            "name": "Tamnougalt",
            "location": "Draa Valley",
            "description": "An ancient kasbah village with earthen architecture, palm groves, and a rich history.",
            "url": "https://en.wikipedia.org/wiki/Tamnougalt",
            "image": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Tamnougalt_Kasbah.jpg"},

        {
            "name": "Imsouane",
            "location": "Atlantic Coast",
            "description": "A tranquil fishing village popular among surfers and seafood lovers, with stunning beaches and views.",
            "url": "https://www.surfertoday.com/travel/imsouane",
            "image": "https://upload.wikimedia.org/wikipedia/commons/1/12/Imsouane_beach.jpg"}
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