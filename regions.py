# Regions in Genshin Impact
overworld_region = [
    "Mondstadt",
    "Liyue",
    "Inazuma",
    "Sumeru",
    "Fontaine",
    "Natlan",
    "Snezhnaya"
]

underworld_region = [
    "Enkanomiya",
    "Bygone Sea",
    "The Chasm"
]

# Information about the regions
overworld_region_info = {
    "Mondstadt": {
        "description": "The City of Freedom",
        "location": "North of the continent",
        "ruler": "Varka",
        "element": "Anemo",
        "notable_characters": ["Diluc", "Venti", "Jean"]
    },
    "Liyue": {
        "description": "The Harbor of Stone and Contracts",
        "location": "East of the continent",
        "ruler": "Zhongli",
        "element": "Geo",
        "notable_characters": ["Zhongli", "Xiangling", "Xingqiu"]
    },
    "Inazuma": {
        "description": "The Nation of Eternity",
        "location": "East of the continent, across the sea",
        "ruler": "Raiden Shogun",
        "element": "Electro",
        "notable_characters": ["Kamisato Ayaka", "Kamisato Kaedehara Kazuha", "Raiden Shogun"]
    },
    "Sumeru": {
        "description": "The Nation of Wisdom",
        "location": "South of the continent",
        "ruler": "Lesser Lord Kusanali",
        "element": "Dendro",
        "notable_characters": ["Tighnari", "Collei", "Dendro Traveler"]
    },
    "Fontaine": {
        "description": "The Nation of Justice",
        "location": "West of the continent",
        "ruler": "Justice of the Harbingers",
        "element": "Hydro",
        "notable_characters": ["Barbara", "Fischl", "Xingqiu"]
    },
    "Natlan": {
        "description": "The Nation of the Sun",
        "location": "West of the continent",
        "ruler": "Unknown",
        "element": "Pyro",
        "notable_characters": ["Klee", "Xiangling", "Hu Tao"]
    },
    "Snezhnaya": {
        "description": "The Nation of the Tsaritsa",
        "location": "North of the continent",
        "ruler": "Tsaritsa of Snezhnaya",
        "element": "Cryo",
        "notable_characters": ["Qiqi", "Rosaria", "Eula"]
    }
}

underworld_region_info = {
    "Enkanomiya": {
        "description": "The Evernight Realm",
        "location": "Under the sea, near Inazuma",
        "ruler": "Unknown",
        "element": "Electro",
        "notable_characters": ["Enjou", "Kokomi"]
    },
    "Bygone Sea": {
        "description": "The Sea of the Past",
        "location": "Under the sea, near Liyue",
        "ruler": "Unknown",
        "element": "Geo",
        "notable_characters": ["Xiangling", "Xingqiu"]
    },
    "The Chasm": {
        "description": "The Underground Nation",
        "location": "Under the continent, near Liyue",
        "ruler": "Unknown",
        "element": "Geo",
        "notable_characters": ["Yun Jin", "Xingqiu"]
    }
}

# Example usage:
def print_region_info(region_name, region_info):
    if region_name in region_info:
        region_data = region_info[region_name]
        print(f"Region: {region_name}")
        print(f"Description: {region_data['description']}")
        print(f"Location: {region_data['location']}")
        print(f"Ruler: {region_data['ruler']}")
        print(f"Element: {region_data['element']}")
        print(f"Notable Characters: {', '.join(region_data['notable_characters'])}")
    else:
        print(f"Region '{region_name}' not found.")

print_region_info("Mondstadt", overworld_region_info)
print_region_info("Enkanomiya", underworld_region_info)
