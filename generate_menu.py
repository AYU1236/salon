import json

data = [
    {
        "category": "Bridal & Engagement Makeup",
        "items": [
            {"name": "Palak’s Signature Bridal Makeup", "desc": "Hd makeup, Hairstyle, Draping, Lenses, Lashes, Nail extension", "price": "15000/-"},
            {"name": "Engagement Makeup", "desc": "Hd Makeup, Hairstyle, Draping, Lenses, Lashes", "price": "11000/-"},
            {"name": "Hd Reception Makeup", "desc": "Hd Makeup, Hairstyle, Draping, Lenses, Lashes. All highends products used (Charlotte Tilbury, Huda, Nars, Anastasia, Mac, one size)", "price": "10000/-"},
            {"name": "Hd Party Makeup", "desc": "Makeup, Hairstyle, Draping, Lenses, Lashes. Product used - Mac, Makeup forever", "price": "6000/-"},
            {"name": "Advance Makeup", "desc": "Makeup, Hairstyle, Draping, Lashes. Product used - Makeup studio, krylon", "price": "4000/-"},
            {"name": "Basic makeup", "desc": "Makeup, Hairstyle, Draping. Product used - Derma, forever52", "price": "2000/-"}
        ]
    },
    {
        "category": "Prebridal Packages (1 Time Service)",
        "items": [
            {"name": "Luxury Package", "desc": "O3 facial, O3 Detan, Rica full body wax, ozone body polishing, premium menicure, Premium pedicure, Threading, Upperlips wax, Forehead wax, Premium hairspa", "price": "10000/-"},
            {"name": "Advance package", "desc": "Aroma Magic facial, Raga detan, White chocolate full body wax, Body care body polishing, Menicure, Pedicure, Upperlips, Forehead thread, Eyebrows, Hairspa", "price": "8000/-"},
            {"name": "Basic package", "desc": "Lotus gold sheen facial, Ozone detan, Honey body wax, Body polishing, Menicure, Pedicure, Upperlips, Eyebrows, Forehead, Basic hairspa", "price": "6000/-"}
        ]
    },
    {
        "category": "Nails Extensions & Art",
        "items": [
            {"name": "Gel nails paints simple (both hands)", "desc": "", "price": "500/-"},
            {"name": "Gel nail paints simple (both feet)", "desc": "", "price": "800/-"},
            {"name": "Glitter Nails paints (Both hands/feet)", "desc": "", "price": "600/- | 800/-"},
            {"name": "Ombre nailpaints (Both hands/feet)", "desc": "", "price": "700/- | 1000/-"},
            {"name": "Cateye nails (Both hands/feet)", "desc": "", "price": "900/- | 1200/-"},
            {"name": "Simple nails extension with gel paints (Both hands/feet)", "desc": "", "price": "1000/- | 1500/-"},
            {"name": "Permanent nail Extensions (Both hands/feet)", "desc": "", "price": "1500/- | 2000/-"},
            {"name": "Permanent nails refilling", "desc": "", "price": "1000/-"},
            {"name": "Temporary nails removal (Both hands/feet)", "desc": "", "price": "500/- | 1000/-"},
            {"name": "Nails removal (Both hands/feet)", "desc": "", "price": "1000/- | 1500/-"},
            {"name": "Nail Add-ons (Temporary / Permanent)", "desc": "Per finger. Glitter (50/100), Cateye (50/100), Ombre (50/100), French (50/100), Stones (30/70), Bows (50/100)", "price": "Varies"}
        ]
    },
    {
        "category": "Waxing Services",
        "items": [
            {"name": "Rica Wax", "desc": "Half hands 300, Full hands 500, Underarms 200, Half leg 400, Full leg 700, Blouse line 500, Back waist line 1200, Stomach 700, Full body 3000", "price": "300/- to 3000/-"},
            {"name": "White Chocolate wax", "desc": "Half hands 200, Full hands 400, Underarms 150, Half leg 300, Full leg 500, Blouse line 300, Back waist 900, Stomach 400, Full body 2500", "price": "150/- to 2500/-"},
            {"name": "Honey wax", "desc": "Half hands 150, Full hands 300, Underarms 100, Half leg 250, Full leg 400, Blouse line 200, Back waist 700, Stomach 300, Full body 2000", "price": "100/- to 2000/-"},
            {"name": "Bikini wax", "desc": "", "price": "1000/-"},
            {"name": "Face wax", "desc": "Eyebrows 150, Forehead 80, Upperlips 60, Chin 70, Sidelock 120, Full face 250", "price": "60/- to 250/-"}
        ]
    },
    {
        "category": "Detan & Bleach",
        "items": [
            {"name": "Ozone Detan", "desc": "Face 500, Neck 400-700, Hands 1500, Legs 1500-2500, Blouse/Waist 700-1500, Stomach 1000, Full body 6000", "price": "400/- to 6000/-"},
            {"name": "Ragga Detan", "desc": "Face 700, Neck 600-1000, Hands 2000, Legs 2000-3500, Blouse/Waist 1000-2000, Stomach 1500, Full body 8500", "price": "600/- to 8500/-"},
            {"name": "O3 Detan", "desc": "Face 900, Neck 700-1300, Hands 3000, Legs 2500-4000, Blouse/Waist 1500-3000, Stomach 2500, Full body 12000", "price": "700/- to 12000/-"},
            {"name": "Normal Bleach", "desc": "Full face 200, Neck 150-300, Hands 700, Legs 900-1500, Blouse/Waist 300-500, Stomach 700, Full body 2500", "price": "150/- to 2500/-"},
            {"name": "Nature Bleach", "desc": "Full face 300, Neck 250-400, Blouseline 400, Waistline 700", "price": "250/- to 700/-"},
            {"name": "Oxy life bleach", "desc": "Full face 400, Neck 300-500, Blouseline 600, Waistline 900", "price": "300/- to 900/-"}
        ]
    },
    {
        "category": "Face Cleanups & Facials",
        "items": [
            {"name": "Face Cleanups", "desc": "Fruit 500, VLCC 700, Lotus 800, Wine 1000, Ragga 1000, Whitening 1200, O3 2000, Aroma 1500", "price": "500/- to 2000/-"},
            {"name": "Basic Facials", "desc": "Normal fruit 700, VLCC (gold/diamond) 1000, Ragga oily skin 1500", "price": "700/- to 1500/-"},
            {"name": "Premium Facials", "desc": "Aroma Magic vit C 1800, Aroma bridal glow 2000, Lotus Instafair 2000, Anti aging 2000", "price": "1800/- to 2000/-"},
            {"name": "Advanced Facials", "desc": "Korean 2500, Whitening 2500, Anti acne 2500, Gold sheen 2500, Acaiberry 2500", "price": "2500/-"},
            {"name": "Luxury Facials", "desc": "O3 bridal glow 3000, Collegen 3000, Glutathione 3000, Casmara 4000", "price": "3000/- to 4000/-"}
        ]
    },
    {
        "category": "Manicure, Pedicure & Thread Work",
        "items": [
            {"name": "Basic Menicure / Pedicure", "desc": "", "price": "500/- | 800/-"},
            {"name": "Premium Menicure / Pedicure", "desc": "", "price": "800/- | 1000/-"},
            {"name": "Detan Menicure / Pedicure", "desc": "", "price": "1000/- | 1500/-"},
            {"name": "Hand / Foot facial (Mani / Pedi)", "desc": "", "price": "1500/- | 2000/-"},
            {"name": "Thread work", "desc": "Eyebrows 50, Forehead 30, Upperlips 30, Chin 40, Sidelock 70, Full face 150", "price": "30/- to 150/-"}
        ]
    },
    {
        "category": "Hair Care & Spa",
        "items": [
            {"name": "Hair wash & Conditioning", "desc": "Normal 300, Loreal 600, Schwarzkopf 800", "price": "300/- to 800/-"},
            {"name": "Hair Spa", "desc": "Normal 800, Loreal 1500, Schwarzkopf 1500", "price": "800/- to 1500/-"},
            {"name": "Hair Spa treatments", "desc": "Protein 1500, Anti dandruff 1500, Hairfall 1500, Fizzy & Dull 1800, Global 2500", "price": "1500/- to 2500/-"},
            {"name": "Head massage & Oiling", "desc": "Coconut with wash 500, Olive with wash 800, Rosemary with wash 1000", "price": "500/- to 1000/-"}
        ]
    },
    {
        "category": "Body Massage & Relax",
        "items": [
            {"name": "Back massage", "desc": "", "price": "1000/-"},
            {"name": "Body oil & massage", "desc": "", "price": "2000/-"},
            {"name": "Body Polishing", "desc": "", "price": "4000/-"}
        ]
    },
    {
        "category": "Hair Cutting & Styling",
        "items": [
            {"name": "Haircutting", "desc": "Trimming 200, Splitends/U Cut/V Cut 300, Advance haircut 500, Baby cutting 200", "price": "200/- to 500/-"},
            {"name": "Blow dry / Straightening", "desc": "Blow dry 500, Straightening 800", "price": "500/- | 800/-"},
            {"name": "Curls & Waves", "desc": "Normal curls 800, Hollywood curls 1000, Wave 1500", "price": "800/- to 1500/-"},
            {"name": "Braids & Buns", "desc": "Messy braids 1500, Simple bun 800, Messy bun 1500, Advance bun 1500", "price": "800/- to 1500/-"},
            {"name": "Hair Extensions", "desc": "", "price": "1500/-"}
        ]
    },
    {
        "category": "Hair Colour & Treatments",
        "items": [
            {"name": "Root touchup", "desc": "Matrix 800, Loreal 1500, Innova 1500, Schwarzkopf 1500", "price": "800/- to 1500/-"},
            {"name": "Global haircolor (Matrix)", "desc": "Above shoulder 2000, Shoulder 4000, Below Shoulder 6000, Waistline 7500", "price": "2000/- to 7500/-"},
            {"name": "Global haircolor (Loreal)", "desc": "Above shoulder 3000, Shoulder 5000, Below shoulder 7000, Waistline 8500", "price": "3000/- to 8500/-"},
            {"name": "Global haircolor (Schwarzkopf)", "desc": "Above shoulder 3500, Shoulder 7000, Below shoulder 8500, Waistline 10000", "price": "3500/- to 10000/-"},
            {"name": "Highlights", "desc": "Per strip 200, 6 strips 1000, 12 strips 2000, 18 strips 3600, Full highlights 2500", "price": "200/- to 3600/-"},
            {"name": "Smoothening", "desc": "Above shoulder 2000, Shoulder 4000, Below shoulder 5500, Waistline 6500", "price": "2000/- to 6500/-"},
            {"name": "Keratin", "desc": "Above shoulder 3000, Shoulder 5000, Below shoulder 7000, Waistline 8500", "price": "3000/- to 8500/-"},
            {"name": "BoTOX / Nanoplastia", "desc": "Above Shoulder 3500, Shoulder 4500, Below Shoulder 5500, Waistline 7000", "price": "3500/- to 7000/-"}
        ]
    }
]

html = "<div class=\"services-menu-container\">\n"
for category in data:
    html += "  <div class=\"services-category reveal\">\n"
    html += f"    <h3 class=\"services-category-title\">{category['category']}</h3>\n"
    html += "    <div class=\"services-list\">\n"
    for item in category['items']:
        html += "      <div class=\"service-item-row\">\n"
        html += "        <div class=\"service-item-info\">\n"
        html += f"          <div class=\"service-item-name\">{item['name']}</div>\n"
        if item['desc']:
            html += f"          <div class=\"service-item-desc\">{item['desc']}</div>\n"
        html += "        </div>\n"
        html += f"        <div class=\"service-item-price\">{item['price']}</div>\n"
        html += "      </div>\n"
    html += "    </div>\n"
    html += "  </div>\n"
html += "</div>\n"

with open("menu_html.txt", "w") as f:
    f.write(html)

print("Menu HTML generated into menu_html.txt")
