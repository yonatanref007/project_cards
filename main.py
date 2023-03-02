from get_df import *

url_to_scrape = "https://shop.tcgplayer.com/price-guide/yugioh/"

html_document = getHTMLdocument(url_to_scrape)

df = get_data_frame(html_document)

one_dim_chart_rarity(df)
writer = pd.ExcelWriter('TTT.xlsx')
df.to_excel(writer)
writer.save()
