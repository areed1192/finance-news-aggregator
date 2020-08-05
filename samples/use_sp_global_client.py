from pprint import pprint

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the SPGlobal News Client.
sp_global_client = news_client.sp_global

# Grab the Methodologies Feed.
content = sp_global_client.methodologies()
pprint(content)

# Grab the All Indicies Feed.
content = sp_global_client.all_indicies()
pprint(content)

# Grab the Research Feed.
content = sp_global_client.research()
pprint(content)

# Grab the Market Commentary Feed.
content = sp_global_client.market_commentary()
pprint(content)

# Grab the Education Feed.
content = sp_global_client.education()
pprint(content)

# Grab the Performance Reports Feed.
content = sp_global_client.performance_reports()
pprint(content)

# Grab the SPIVA Feed.
content = sp_global_client.spiva()
pprint(content)

# Grab the Index TV Feed.
content = sp_global_client.index_tv()
pprint(content)

# Grab the Corporate News Feed.
content = sp_global_client.corporate_news()
pprint(content)

# Grab the Index Launches Feed.
content = sp_global_client.index_launches()
pprint(content)

# Grab the Index Announcements Feed.
content = sp_global_client.index_announcments()
pprint(content)

# Grab the New Consultations Feed.
content = sp_global_client.new_counsultations()
pprint(content)