"""Remove old table of crops

Revision ID: c8d2e229d288
Revises: ec89eea99566
Create Date: 2023-01-25 07:31:38.631780

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import String, Integer
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = "c8d2e229d288"
down_revision = "ec89eea99566"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table("crop")


def downgrade():
    crops = [
        {"crop_code": 0, "crop_name": "Not a crop"},
        {"crop_code": 1, "crop_name": "Alfalfa"},
        {"crop_code": 2, "crop_name": "Almond"},
        {"crop_code": 3, "crop_name": "Anise seeds"},
        {"crop_code": 4, "crop_name": "Apple"},
        {"crop_code": 5, "crop_name": "Apricot"},
        {"crop_code": 6, "crop_name": "Arracha"},
        {"crop_code": 7, "crop_name": "Arrowroot"},
        {"crop_code": 8, "crop_name": "Artichoke"},
        {"crop_code": 9, "crop_name": "Asparagus"},
        {"crop_code": 10, "crop_name": "Avocado"},
        {"crop_code": 11, "crop_name": "Bergamot"},
        {"crop_code": 12, "crop_name": "Betel nut"},
        {"crop_code": 13, "crop_name": "Black pepper"},
        {"crop_code": 14, "crop_name": "Black wattle"},
        {"crop_code": 15, "crop_name": "Brazil nut"},
        {"crop_code": 16, "crop_name": "Breadfruit"},
        {"crop_code": 17, "crop_name": "Broccoli"},
        {"crop_code": 18, "crop_name": "Brussels sprouts"},
        {"crop_code": 19, "crop_name": "Buckwheat"},
        {"crop_code": 20, "crop_name": "Cabbage"},
        {"crop_code": 21, "crop_name": "Cantaloupe"},
        {"crop_code": 22, "crop_name": "Caraway seeds"},
        {"crop_code": 23, "crop_name": "Cardamom"},
        {"crop_code": 24, "crop_name": "Cardoon"},
        {"crop_code": 25, "crop_name": "Carob"},
        {"crop_code": 26, "crop_name": "Carrot"},
        {"crop_code": 27, "crop_name": "Cashew nuts"},
        {"crop_code": 28, "crop_name": "Castor bean"},
        {"crop_code": 29, "crop_name": "Cauliflower"},
        {"crop_code": 30, "crop_name": "Cassava"},
        {"crop_code": 31, "crop_name": "Celery"},
        {"crop_code": 32, "crop_name": "Chayote"},
        {"crop_code": 33, "crop_name": "Cherry"},
        {"crop_code": 34, "crop_name": "Chestnut"},
        {"crop_code": 35, "crop_name": "Chickpea"},
        {"crop_code": 36, "crop_name": "Chicory"},
        {"crop_code": 37, "crop_name": "Cinnamon"},
        {"crop_code": 38, "crop_name": "Citron"},
        {"crop_code": 39, "crop_name": "Citronella"},
        {"crop_code": 40, "crop_name": "Clementine"},
        {"crop_code": 41, "crop_name": "Clove"},
        {"crop_code": 42, "crop_name": "Clover"},
        {"crop_code": 43, "crop_name": "Cocoa"},
        {"crop_code": 44, "crop_name": "Coconut"},
        {"crop_code": 45, "crop_name": "Cocoyam"},
        {"crop_code": 46, "crop_name": "Coffee"},
        {"crop_code": 47, "crop_name": "Cola"},
        {"crop_code": 48, "crop_name": "Corn salad"},
        {"crop_code": 49, "crop_name": "Cottonseed"},
        {"crop_code": 50, "crop_name": "Cowpea"},
        {"crop_code": 51, "crop_name": "Cranberry"},
        {"crop_code": 52, "crop_name": "Cress"},
        {"crop_code": 53, "crop_name": "Cucumber"},
        {"crop_code": 54, "crop_name": "Custard apple"},
        {"crop_code": 55, "crop_name": "Dates"},
        {"crop_code": 56, "crop_name": "Drumstick tree"},
        {"crop_code": 57, "crop_name": "Bean"},
        {"crop_code": 58, "crop_name": "Durum wheat"},
        {"crop_code": 59, "crop_name": "Earth pea (bambara groundnut)"},
        {"crop_code": 60, "crop_name": "Edo (eddoe)"},
        {"crop_code": 61, "crop_name": "Eggplant"},
        {"crop_code": 62, "crop_name": "Endive"},
        {"crop_code": 63, "crop_name": "Fennel"},
        {"crop_code": 64, "crop_name": "Fenugreek"},
        {"crop_code": 65, "crop_name": "Fig"},
        {"crop_code": 66, "crop_name": "Fique"},
        {"crop_code": 67, "crop_name": "Garlic"},
        {"crop_code": 68, "crop_name": "Geranium"},
        {"crop_code": 69, "crop_name": "Ginger"},
        {"crop_code": 70, "crop_name": "Gooseberry"},
        {"crop_code": 71, "crop_name": "Gourd"},
        {"crop_code": 72, "crop_name": "Grapefruit"},
        {"crop_code": 73, "crop_name": "Grapes"},
        {"crop_code": 74, "crop_name": "Grass esparto"},
        {"crop_code": 75, "crop_name": "Green bean"},
        {"crop_code": 76, "crop_name": "Guava"},
        {"crop_code": 77, "crop_name": "Hazelnut"},
        {"crop_code": 78, "crop_name": "Hemp seed"},
        {"crop_code": 79, "crop_name": "Henequen"},
        {"crop_code": 80, "crop_name": "Henna"},
        {"crop_code": 81, "crop_name": "Hop"},
        {"crop_code": 82, "crop_name": "Horse bean"},
        {"crop_code": 83, "crop_name": "Horseradish"},
        {"crop_code": 84, "crop_name": "Indigo"},
        {"crop_code": 85, "crop_name": "Jasmine"},
        {"crop_code": 86, "crop_name": "Jute"},
        {"crop_code": 87, "crop_name": "Kale"},
        {"crop_code": 88, "crop_name": "Kapok"},
        {"crop_code": 89, "crop_name": "Kenaf"},
        {"crop_code": 90, "crop_name": "Kohlrabi"},
        {"crop_code": 91, "crop_name": "Lavender"},
        {"crop_code": 92, "crop_name": "Leek"},
        {"crop_code": 93, "crop_name": "Lemon"},
        {"crop_code": 94, "crop_name": "Lemon grass"},
        {"crop_code": 95, "crop_name": "Lentil"},
        {"crop_code": 96, "crop_name": "Lespedeza"},
        {"crop_code": 97, "crop_name": "Lettuce"},
        {"crop_code": 98, "crop_name": "Linseed"},
        {"crop_code": 99, "crop_name": "Liquorice"},
        {"crop_code": 100, "crop_name": "Litchi"},
        {"crop_code": 101, "crop_name": "Loquat"},
        {"crop_code": 102, "crop_name": "Lupine"},
        {"crop_code": 103, "crop_name": "Macadamia"},
        {"crop_code": 104, "crop_name": "Mace"},
        {"crop_code": 105, "crop_name": "Maguey"},
        {"crop_code": 106, "crop_name": "Mango"},
        {"crop_code": 107, "crop_name": "Manila hemp (abaca)"},
        {"crop_code": 108, "crop_name": "Medlar"},
        {"crop_code": 109, "crop_name": "Millet"},
        {"crop_code": 110, "crop_name": "Millet, Italian"},
        {"crop_code": 111, "crop_name": "Millet, Japanese"},
        {"crop_code": 112, "crop_name": "Millet, finger"},
        {"crop_code": 113, "crop_name": "Millet, pearl"},
        {"crop_code": 114, "crop_name": "Millet, proso"},
        {"crop_code": 115, "crop_name": "Mint"},
        {"crop_code": 116, "crop_name": "Mulberry for fruit"},
        {"crop_code": 117, "crop_name": "Mulberry for silkworms"},
        {"crop_code": 118, "crop_name": "Mushrooms"},
        {"crop_code": 119, "crop_name": "Mustard"},
        {"crop_code": 120, "crop_name": "New Zealand flax (formio)"},
        {"crop_code": 121, "crop_name": "Niger seed"},
        {"crop_code": 122, "crop_name": "Nutmeg"},
        {"crop_code": 123, "crop_name": "Oats"},
        {"crop_code": 124, "crop_name": "Okra"},
        {"crop_code": 125, "crop_name": "Olive"},
        {"crop_code": 126, "crop_name": "Onion"},
        {"crop_code": 127, "crop_name": "Orange"},
        {"crop_code": 128, "crop_name": "Orange, bitter"},
        {"crop_code": 129, "crop_name": "Orchard grass"},
        {"crop_code": 130, "crop_name": "Palm oil"},
        {"crop_code": 131, "crop_name": "Palmyra palm"},
        {"crop_code": 132, "crop_name": "Papaya (pawpaw)"},
        {"crop_code": 133, "crop_name": "Parsnip"},
        {"crop_code": 134, "crop_name": "Pea"},
        {"crop_code": 135, "crop_name": "Peach"},
        {"crop_code": 136, "crop_name": "Peanut"},
        {"crop_code": 137, "crop_name": "Pear"},
        {"crop_code": 138, "crop_name": "Pecan nut"},
        {"crop_code": 139, "crop_name": "Pepper (Capsicum)"},
        {"crop_code": 140, "crop_name": "Persimmon"},
        {"crop_code": 141, "crop_name": "Pigeon pea"},
        {"crop_code": 142, "crop_name": "Pineapple"},
        {"crop_code": 143, "crop_name": "Pistachio nut"},
        {"crop_code": 144, "crop_name": "Plantain"},
        {"crop_code": 145, "crop_name": "Pomegranate"},
        {"crop_code": 146, "crop_name": "Pomelo"},
        {"crop_code": 147, "crop_name": "Poppy seed"},
        {"crop_code": 148, "crop_name": "Potato"},
        {"crop_code": 149, "crop_name": "Prune"},
        {"crop_code": 150, "crop_name": "Pyrethum"},
        {"crop_code": 151, "crop_name": "Quebracho"},
        {"crop_code": 152, "crop_name": "Quince"},
        {"crop_code": 153, "crop_name": "Quinine"},
        {"crop_code": 154, "crop_name": "Quinoa"},
        {"crop_code": 155, "crop_name": "Radish"},
        {"crop_code": 156, "crop_name": "Ramie"},
        {"crop_code": 157, "crop_name": "Raspberry"},
        {"crop_code": 158, "crop_name": "Redtop"},
        {"crop_code": 159, "crop_name": "Rhea"},
        {"crop_code": 160, "crop_name": "Rhubarb"},
        {"crop_code": 161, "crop_name": "Rice"},
        {"crop_code": 162, "crop_name": "Rose"},
        {"crop_code": 163, "crop_name": "Rubber"},
        {"crop_code": 164, "crop_name": "Ryegrass seed"},
        {"crop_code": 165, "crop_name": "Safflower seed"},
        {"crop_code": 166, "crop_name": "Sago palm"},
        {"crop_code": 167, "crop_name": "Sainfoin"},
        {"crop_code": 168, "crop_name": "Salsify"},
        {"crop_code": 169, "crop_name": "Sapodilla"},
        {"crop_code": 170, "crop_name": "Savoy cabbage"},
        {"crop_code": 171, "crop_name": "Scorzonera"},
        {"crop_code": 172, "crop_name": "Sesame"},
        {"crop_code": 173, "crop_name": "Shea butter"},
        {"crop_code": 174, "crop_name": "Sisal"},
        {"crop_code": 175, "crop_name": "Sorghum"},
        {"crop_code": 176, "crop_name": "Sour lime"},
        {"crop_code": 177, "crop_name": "Soybean"},
        {"crop_code": 178, "crop_name": "Spelt"},
        {"crop_code": 179, "crop_name": "Spinach"},
        {"crop_code": 180, "crop_name": "Barley"},
        {"crop_code": 181, "crop_name": "Squash"},
        {"crop_code": 182, "crop_name": "Strawberry"},
        {"crop_code": 183, "crop_name": "Sudan grass"},
        {"crop_code": 184, "crop_name": "Beet"},
        {"crop_code": 185, "crop_name": "Sugarcane"},
        {"crop_code": 186, "crop_name": "Sunflower"},
        {"crop_code": 187, "crop_name": "Sunhemp"},
        {"crop_code": 188, "crop_name": "Swede"},
        {"crop_code": 189, "crop_name": "Maize"},
        {"crop_code": 190, "crop_name": "Sweet lime"},
        {"crop_code": 191, "crop_name": "Sweet pepper"},
        {"crop_code": 192, "crop_name": "Sweet potato"},
        {"crop_code": 193, "crop_name": "Sweet sorghum"},
        {"crop_code": 194, "crop_name": "Tangerine"},
        {"crop_code": 195, "crop_name": "Tannia"},
        {"crop_code": 196, "crop_name": "Taro"},
        {"crop_code": 197, "crop_name": "Tea"},
        {"crop_code": 198, "crop_name": "Teff"},
        {"crop_code": 199, "crop_name": "Timothy"},
        {"crop_code": 200, "crop_name": "Tobacco"},
        {"crop_code": 201, "crop_name": "Tomato"},
        {"crop_code": 202, "crop_name": "Trefoil"},
        {"crop_code": 203, "crop_name": "Tung tree"},
        {"crop_code": 204, "crop_name": "Turnip"},
        {"crop_code": 205, "crop_name": "Urena (Congo jute)"},
        {"crop_code": 206, "crop_name": "Vanilla"},
        {"crop_code": 207, "crop_name": "Vetch"},
        {"crop_code": 208, "crop_name": "Walnut"},
        {"crop_code": 209, "crop_name": "Watermelon"},
        {"crop_code": 210, "crop_name": "Wheat"},
        {"crop_code": 211, "crop_name": "White cabbage"},
        {"crop_code": 212, "crop_name": "Chili pepper"},
        {"crop_code": 213, "crop_name": "Winter rye"},
        {"crop_code": 214, "crop_name": "Winter wheat"},
        {"crop_code": 215, "crop_name": "Yams"},
        {"crop_code": 216, "crop_name": "Yerba mate"},
        {"crop_code": 217, "crop_name": "Basil"},
        {"crop_code": 218, "crop_name": "Cumin"},
        {"crop_code": 219, "crop_name": "Banana"},
        {"crop_code": 220, "crop_name": "Dill"},
        {"crop_code": 221, "crop_name": "Faba bean"},
        {"crop_code": 222, "crop_name": "Amaranth"},
        {"crop_code": 223, "crop_name": "Lettuce"},
        {"crop_code": 224, "crop_name": "Arugula"},
    ]

    op.create_table(
        "crop",
        sa.Column("crop_code", sa.Integer(), nullable=False, autoincrement=False),
        sa.Column("crop_name", sa.Unicode(length=45), nullable=False),
        sa.PrimaryKeyConstraint("crop_code", name=op.f("pk_crop")),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )

    crop_table = table(
        "crop",
        column("crop_code", Integer),
        column("crop_name", String),
    )
    op.bulk_insert(crop_table, crops)
