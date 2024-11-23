from flask import Flask, render_template, request 
app = Flask(__name__)
activities = {
"Outdoor Adventures": [ # category 01
    {
        "name": "Camel Trekking in the Sahara Desert",
        "location": "Merzouga",
        "description": "Explore the vast dunes of Erg Chebbi on camelback, experiencing the beauty of the desert and its golden sands.",
        "url": "https://www.visitmorocco.com/en/travel/sahara",
        "image": "https://www.bing.com/images/search?view=detailV2&ccid=SZE7kEFS&id=317F3172575A66AEB6EA48E9E1D846A593B5DCE9&thid=OIP.SZE7kEFSniAve2cdujnpIwEsCI&mediaurl=https%3a%2f%2fwww.mouhoutours.com%2fwp-content%2fuploads%2f2019%2f05%2fcamel-trek-sahara-desert.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.49913b9041529e202f7b671dba39e923%3frik%3d6dy1k6VG2OHpSA%26pid%3dImgRaw%26r%3d0&exph=1806&expw=3977&q=Camel+Trekking+in+the+Sahara+Desert&simid=608050263466996429&FORM=IRPRST&ck=E0A7E73DDA9C52672DFE59B5DEA4A04B&selectedIndex=1&itb=0"},

    {
        "name": "Hiking in the High Atlas Mountains",
        "location": "Imlil, near Mount Toubkal",
        "description": "Discover breathtaking trails, traditional Berber villages, and stunning mountain landscapes.",
        "url": "https://www.trekkinginmorocco.com/",
        "image": "https://www.bing.com/images/search?view=detailV2&ccid=sQ5Xpbik&id=FD8E0971A345970296C01A6E8E8468456941F36A&thid=OIP.sQ5Xpbik-7uYBcW7LCwZVQHaGo&mediaurl=https%3a%2f%2fi.pinimg.com%2foriginals%2f16%2f59%2fcf%2f1659cfb21bc3b94179450ea614bdf919.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.b10e57a5b8a4fbbb9805c5bb2c2c1955%3frik%3davNBaUVohI5uGg%26pid%3dImgRaw%26r%3d0&exph=916&expw=1024&q=Hiking+in+the+High+Atlas+Mountains&simid=607999501242617348&FORM=IRPRST&ck=37C5FCCB456F88769899FA6D795587E1&selectedIndex=4&itb=0"},
    
    {
        "name": "Surfing in Taghazout",
        "location": "Taghazout, near Agadir",
        "description": "Enjoy world-class surfing on Morocco's Atlantic coast with a laid-back beach town vibe.",
        "url": "https://www.surfmaroc.com/",
        "image": "https://www.bing.com/images/search?view=detailV2&ccid=M6VgUo5R&id=EB8BEA77E3195C7796674FACEC7478319CAE603C&thid=OIP.M6VgUo5RAcJV12BgzwjjcwHaFS&mediaurl=https%3a%2f%2fsurfparadisemorocco.net%2fwp-content%2fuploads%2f2022%2f08%2fTaghazout-1.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.33a560528e5101c255d76060cf08e373%3frik%3dPGCunDF4dOysTw%26pid%3dImgRaw%26r%3d0&exph=572&expw=800&q=Surfing+in+Taghazout&simid=607986350106894647&FORM=IRPRST&ck=D30534079268F6892C7D0077D250946F&selectedIndex=1&itb=0"},

    {
        "name": "Hot Air Balloon Ride over Marrakech",
        "location": "Marrakech",
        "description": "Soar above the Red City and surrounding landscapes for an unforgettable sunrise experience.",
        "url": "https://www.ciel-marrakech.com/en/",
        "image": "https://www.bing.com/images/search?view=detailV2&ccid=DXLpPm1w&id=027F58A02E88987126C9D1E3BDE75DFC3ABB9CB1&thid=OIP.DXLpPm1w9fpXm7I-QC_g6wHaFj&mediaurl=https%3a%2f%2fepic.travel%2fwp-content%2fuploads%2f2019%2f04%2f530-hot-air-balloon-marrakech-2-1024x768.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.0d72e93e6d70f5fa579bb23e402fe0eb%3frik%3dsZy7Ovxd573j0Q%26pid%3dImgRaw%26r%3d0&exph=768&expw=1024&q=Hot+Air+Balloon+Ride+over+Marrakech&simid=608054953562813213&FORM=IRPRST&ck=2FEC2B3209E6AC783E01764449B53A6C&selectedIndex=0&itb=0"},

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
        "image": "https://www.bing.com/images/search?view=detailV2&ccid=w5hcMcYs&id=A72AECDE3B76F67F887CE76069833D991BC94D6D&thid=OIP.w5hcMcYscpSVYQKnNv88JAHaEK&mediaurl=https%3a%2f%2fmajatravels.com%2fwp-content%2fuploads%2f2023%2f04%2fclimbing-todra-sport-scaled.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.c3985c31c62c7294956102a736ff3c24%3frik%3dbU3JG5k9g2lg5w%26pid%3dImgRaw%26r%3d0&exph=1440&expw=2560&q=Climbing+in+Todra+Gorge&simid=608019417016066660&FORM=IRPRST&ck=0CE70980E3209FD359E10E526293CB12&selectedIndex=0&itb=0"},

    {
        "name": "Exploring the Blue Streets of Chefchaouen",
        "location": "Chefchaouen",
        "description": "Stroll through the picturesque blue-painted streets of this serene mountain town.",
        "url": "https://www.visitmorocco.com/en/travel/chefchaouen",
        "image": "https://www.bing.com/images/search?view=detailV2&ccid=QSac1Zfv&id=426502495DE4E20201AFFC8925FE860986317362&thid=OIP.QSac1Zfvdkt6G9VVWAS1GwHaE8&mediaurl=https%3a%2f%2fwww.traveltalktours.com%2fwp-content%2fuploads%2f2022%2f03%2fmilad-alizadeh-JibMa0FbyHw-unsplash-1024x683.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.41269cd597ef764b7a1bd5555804b51b%3frik%3dYnMxhgmG%252fiWJ%252fA%26pid%3dImgRaw%26r%3d0&exph=683&expw=1024&q=Exploring+the+Blue+Streets+of+Chefchaouen&simid=608042219005050479&FORM=IRPRST&ck=D43207C010B8E7E8D73455ED122E1B02&selectedIndex=2&itb=0"},

    {
        "name": "Windsurfing in Essaouira",
        "location": "Essaouira",
        "description": "Experience strong Atlantic winds perfect for windsurfing and kiteboarding in this charming coastal city.",
        "url": "https://www.essaouira.com/",
        "image": "https://www.bing.com/images/search?view=detailV2&ccid=8AX9E5rH&id=EFECF6EFDD2276AB02E1CFDA7E666B2A6080BE6F&thid=OIP.8AX9E5rHU5-bk0MhAmSfwQHaE7&mediaurl=https%3a%2f%2fwww.sportif.travel%2fimages%2fuploads%2fcentres%2fEssaouira%2fWS%2f5_Morocco_Essaouira_Windsurf_Kitesurf_Holiday_Action_Kitesurf_Lesson_800x533.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.f005fd139ac7539f9b93432102649fc1%3frik%3db76AYCprZn7azw%26pid%3dImgRaw%26r%3d0&exph=533&expw=800&q=Windsurfing+in+Essaouira&simid=608040896112959746&FORM=IRPRST&ck=9C1FD7266CC33C2FBBA2CCDE0C4C6F35&selectedIndex=1&itb=0"},

    {
        "name": "Horseback Riding in Souss Massa National Park",
        "location": "Souss Massa National Park, near Agadir",
        "description": "Ride through coastal dunes and spot unique wildlife, including gazelles and flamingos.",
        "url": "https://www.visitmorocco.com/en/travel/souss-massa-national-park",
        "image": "https://www.bing.com/images/search?view=detailV2&ccid=PeC8v87p&id=F78EAE8A3D38CA498BCA20864FCD5C6458F6B241&thid=OIP.PeC8v87pa2Xzf4V-JssjDQHaE7&mediaurl=https%3a%2f%2fwww.stunningtravel.nl%2fwp-content%2fuploads%2f2021%2f02%2fSouss-Massa-National-Park-696x463.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.3de0bcbfcee96b65f37f857e26cb230d%3frik%3dQbL2WGRczU%252bGIA%26pid%3dImgRaw%26r%3d0%26sres%3d1%26sresct%3d1%26srh%3d800%26srw%3d1202&exph=463&expw=696&q=Horseback+Riding+in+Souss+Massa+National+Park&simid=608002018128574727&FORM=IRPRST&ck=D6E9509CCEBD238B3869C75B30492C76&selectedIndex=6&itb=0"},
        
    {
        "name": "Caving at Friouato Caves",
        "location": "Taza",
        "description": "Descend into Morocco's largest cave system and explore its fascinating geological formations.",
        "url": "https://www.moroccoworldnews.com/2020/12/328366/friouato-caves-taza-a-hidden-natural-wonder-in-morocco/",
        "image": "https://www.bing.com/images/search?view=detailV2&ccid=lu4n0iAL&id=7B23CB38F9E36A145A476B462AC8D45EE7F3EADB&thid=OIP.lu4n0iALZGY8Hc0pG8HnoQHaE5&mediaurl=https%3a%2f%2f1.bp.blogspot.com%2f-di5wg06hXIU%2fXcm0cZWrb-I%2fAAAAAAAAGoU%2fp2Y1mqdEK7UDqvdqqFo5QeOt0q3nwz5igCLcBGAsYHQ%2fs1600%2ffrou.PNG&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.96ee27d2200b64663c1dcd291bc1e7a1%3frik%3d2%252brz517UyCpGaw%26pid%3dImgRaw%26r%3d0&exph=367&expw=555&q=Caving+at+Friouato+Caves&simid=608048635666505527&FORM=IRPRST&ck=30902B89A11E2F575560625780308ED3&selectedIndex=1&itb=0"
        }
    ],
    #************************************
    "Historical Sites": [ # category 02
        {
            "name": "Hassan II Mosque",
            "location": "Casablanca",
            "description": "The largest mosque in Morocco, renowned for its stunning architecture and seaside location.",
            "url": "https://en.wikipedia.org/wiki/Hassan_II_Mosque",
            "image": "https://images.pexels.com/photos/20070479/pexels-photo-20070479/free-photo-of-hassan-ii-mosque-in-casablanca-in-morocco.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},

        {
            "name": "Volubilis",
            "location": "Near Meknes",
            "description": "A well-preserved Roman city and UNESCO World Heritage site, featuring stunning mosaics and ruins.",
            "url": "https://en.wikipedia.org/wiki/Volubilis",
            "image": "https://images.pexels.com/photos/11517326/pexels-photo-11517326.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},

        {
            "name": "Aït Benhaddou",
            "location": "Ouarzazate",
            "description": "A fortified village and UNESCO site, famous for its earthen buildings and appearances in movies like 'Gladiator.'",
            "url": "https://en.wikipedia.org/wiki/A%C3%AFt_Benhaddou",
            "image": "https://images.pexels.com/photos/3581916/pexels-photo-3581916.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},

        {
            "name": "El Badi Palace",
            "location": "Marrakech",
            "description": "Ruins of a once-grand palace showcasing Saadian Dynasty architecture and history.",
            "url": "https://en.wikipedia.org/wiki/El_Badi_Palace",
            "image": "https://images.pexels.com/photos/18375222/pexels-photo-18375222/free-photo-of-view-of-the-annex-on-the-northwest-side-of-the-el-badi-palace-in-marrakesh-morocco.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},

        {
            "name": "Saadian Tombs",
            "location": "Marrakech",
            "description": "A hidden necropolis dating back to the Saadian Dynasty, famous for its intricate decoration.",
            "url": "https://en.wikipedia.org/wiki/Saadian_Tombs",
            "image": "https://images.pexels.com/photos/20740159/pexels-photo-20740159/free-photo-of-flower-bush-growing-by-entrance-to-saadian-tombs-in-marrakech-morocco.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},

        {
            "name": "Chellah",
            "location": "Rabat",
            "description": "An ancient necropolis and Roman ruin located in the capital city of Morocco.",
            "url": "https://en.wikipedia.org/wiki/Chellah",
            "image": "https://images.pexels.com/photos/19061686/pexels-photo-19061686/free-photo-of-narrow-alley-in-town-in-morocco.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},

        {
            "name": "Bahia Palace",
            "location": "Marrakech",
            "description": "A 19th-century palace showcasing stunning Moroccan architecture and lush gardens.",
            "url": "https://en.wikipedia.org/wiki/Bahia_Palace",
            "image": "https://www.pexels.com/photo/bahia-palace-in-marrakesh-morocco-4220977/"},

        {
            "name": "Kasbah of the Udayas",
            "location": "Rabat",
            "description": "A historic kasbah with picturesque streets, Andalusian gardens, and ocean views.",
            "url": "https://en.wikipedia.org/wiki/Kasbah_of_the_Udayas",
            "image": "https://images.pexels.com/photos/2958597/pexels-photo-2958597.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},

        {
            "name": "Fez Medina (Fes el Bali)",
            "location": "Fez",
            "description": "One of the oldest and largest medieval cities in the world, and a UNESCO World Heritage site.",
            "url": "https://en.wikipedia.org/wiki/Fes_el_Bali",
            "image": "https://images.pexels.com/photos/5472521/pexels-photo-5472521.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},

        {
            "name": "Mausoleum of Mohammed V",
            "location": "Rabat",
            "description": "The tomb of King Mohammed V, featuring intricate Moroccan artistry and history.",
            "url": "https://en.wikipedia.org/wiki/Mausoleum_of_Mohammed_V",
            "image": "https://images.pexels.com/photos/9208231/pexels-photo-9208231.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        }
    ],
    #************************************
    "Food & Drink": [ # category 03
        {
            "name": "Tagine Cooking Experience",
            "location": "Marrakech",
            "description": "Learn to prepare Morocco’s iconic slow-cooked dish, rich in spices and flavors, in a traditional tagine pot.",
            "url": "https://www.cookingclassmaroc.com",
            "image": "https://www.pexels.com/photo/person-holding-purple-ceramic-lid-2287528/" },
        {
            "name": "Moroccan Mint Tea Ceremony",
            "location": "Fez",
            "description": "Experience the art of pouring and drinking traditional mint tea, a symbol of hospitality in Morocco.",
            "url": "https://en.wikipedia.org/wiki/Maghrebi_mint_tea",
            "image": "https://www.pexels.com/photo/person-pouring-tea-cup-glass-near-brown-curtain-1618904/"},
            
        {
            "name": "Djemaa el-Fna Food Stalls",
            "location": "Marrakech",
            "description": "Sample a variety of Moroccan street food in the bustling main square, from grilled meats to pastries.",
            "url": "https://www.visitmorocco.com/en/marrakech",
            "image": "https://images.pexels.com/photos/3243027/pexels-photo-3243027.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        },
        {
            "name": "Harira Soup Tasting",
            "location": "Casablanca",
            "description": "Try Morocco’s traditional soup, made with lentils, chickpeas, and spices, often served during Ramadan.",
            "url": "https://www.marocmama.com/moroccan-harira-soup-recipe/",
            "image": "https://www.pexels.com/photo/a-bowl-of-pumpkin-soup-6853457/"},

        {
            "name": "Couscous Fridays",
            "location": "Rabat",
            "description": "Enjoy authentic couscous, a staple dish traditionally served on Fridays, made with fluffy grains and vegetables.",
            "url": "https://en.wikipedia.org/wiki/Couscous",
            "image": "https://tasteofmaroc.com/wp-content/uploads/2017/10/couscous-hayat-2-740x545.jpg.webp"},

        {
            "name": "Seafood at Agadir Marina",
            "location": "Agadir",
            "description": "Savor fresh seafood at waterfront restaurants, from grilled fish to fried calamari.",
            "url": "https://www.tripadvisor.com/Restaurants-g293731-c33-Agadir_Souss_Massa.html",
            "image": "https://tasteofmaroc.com/wp-content/uploads/2018/08/seafood-bastilla-bigstock-picturepartners-740x493.jpg.webp"},

        {
            "name": "Pastilla Feast",
            "location": "Fez",
            "description": "Taste this sweet and savory pastry filled with spiced chicken or pigeon, almonds, and cinnamon.",
            "url": "https://en.wikipedia.org/wiki/Bastilla",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=SAsbp%2frT&id=CFF83B65EF4BDAB8D8DCF8DC8AB034B952DAFC3E&thid=OIP.SAsbp_rTR2t0GC7KMjy2aQHaEK&mediaurl=https%3a%2f%2fwww.mjtnews.com%2fwp-content%2fuploads%2f2020%2f09%2f5316136140001_6007131285001_6007124510001-vs-2.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.480b1ba7fad3476b74182eca323cb669%3frik%3dPvzaUrk0sIrc%252bA%26pid%3dImgRaw%26r%3d0&exph=1080&expw=1920&q=pastilla+Feast+morocco&simid=608031253929881545&FORM=IRPRST&ck=4893F6283287BC4385B7818374793329&selectedIndex=3&itb=0"},

        {
            "name": "Visit an Argan Oil Cooperative",
            "location": "Essaouira",
            "description": "Learn about and taste argan oil, a versatile Moroccan product used for cooking and cosmetics.",
            "url": "https://www.lonelyplanet.com/articles/moroccan-argan-oil",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=rvWoVu5j&id=27444A2B6C37426E4313841DDDC1E42D662D1B6A&thid=OIP.rvWoVu5jJOTA3xKaekLK5gHaFj&mediaurl=https%3a%2f%2fwww.culturecherifienne.com%2fwp-content%2fuploads%2f2018%2f04%2fcoop%c3%a9rative-arganier-femmes-1024x768.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.aef5a856ee6324e4c0df129a7a42cae6%3frik%3dahstZi3kwd0dhA%26pid%3dImgRaw%26r%3d0&exph=768&expw=1024&q=Visit+an+Argan+Oil+Cooperative&simid=608056297853226584&FORM=IRPRST&ck=B7FFE3873C7774BE967F7027857525A4&selectedIndex=7&itb=0"},

        {
            "name": "Moroccan Pastries Tasting",
            "location": "Meknes",
            "description": "Sample traditional sweets like *chebakia* (fried sesame cookies) and *ghriba* (almond biscuits).",
            "url": "https://tasteatlas.com/moroccan-desserts",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=0b%2b9wbQ3&id=0D809D09D58B55D7E5D81EFFD4547873521F7286&thid=OIP.0b-9wbQ3pkVIupxT1alGwQHaE8&mediaurl=https%3a%2f%2fi.pinimg.com%2foriginals%2f8b%2f32%2fa5%2f8b32a5ea233f38ca58fd236c7bbf7648.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.d1bfbdc1b437a64548ba9c53d5a946c1%3frik%3dhnIfUnN4VNT%252fHg%26pid%3dImgRaw%26r%3d0&exph=2304&expw=3456&q=Moroccan+Pastries+Tasting&simid=608011432704937619&FORM=IRPRST&ck=D57229EB0933BF8482E6B142613C4C70&selectedIndex=39&itb=0"},

        {
            "name": "Visit a Traditional Riad for Dinner",
            "location": "Chefchaouen",
            "description": "Enjoy a multi-course Moroccan meal in the courtyard of a traditional riad, surrounded by beautiful décor.",
            "url": "https://www.riadchefchaouen.com",
            "image": "https://www.bing.com/images/search?view=detailV2&ccid=YpKWN7Tr&id=44E26D9BBC322A0BBAB7EA0D6BE34703EC4CF681&thid=OIP.YpKWN7TrdqZY3oe0FkFWFgHaE7&mediaurl=https%3a%2f%2fimages.musement.com%2fcover%2f0081%2f46%2fthumb_8045901_cover_header.jpeg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.62929637b4eb76a658de87b416415616%3frik%3dgfZM7ANH42sN6g%26pid%3dImgRaw%26r%3d0&exph=1333&expw=2000&q=Visit+a+Traditional+Riad+for+Dinner&simid=608010852846737742&FORM=IRPRST&ck=6A6A8D16DA16457F3CD7F41CF218A652&selectedIndex=3&itb=0"}
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