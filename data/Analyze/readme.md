# Topic Labels

## Constraints
These labels are interpretive and are most reliable when a topic is assigned to  at least 10% of the words in a document (approximately). 

## Labeling Method
The topic labels were assigned based on looking at the words of the topic and the documents in which those topics were most prominent. The lists of documents examined was created in [link to notebook](). In cases of ambiguity, I used the topic model browser to explore the context of the topic in question, such as peaks in time and other topics assigned to the identified documents, to narrow my interpretation of the word usage captured by the topic.

In addition to individual topic topic names, I assigned each topic to one of 34 general category labels. I used these to aggregate the topics, so as to better see broad trends, which are difficult to visualize with 250 individual topics. 

## Features
Features of the "Topic Labels" data set.

### mallet_topic_id
ID number given to the topic by MALLET. These number are arbitrary.

### browser_topic_id
The DfR topic model browser counts from 1 rather than from 0. The topic id for the browser is the MALLET ID +1.

### topic_label
The topic label is an interpreted label based on the `topic_word` and the documents where the topic was prevalent. The label has 2 - 3 parts. The first part is the category; the second, inside the "()" provides more details about the particular content; the third, when used, provided further clarification using the dash "-".

### topic_category
The topic category provides one of 34 categories in which I grouped the topics in order to aggregate the prevalence of related topics. This provides a means of coping with the details provided by a 250 topic model.

The category options are:
+ advertisements: Advertisements feature frequently within the pages of the denominational periodicals, and particularly within the health-related titles. These are often for other periodical available to purchase on subscription, as well as other books and tracts published by the denomination. Additionally, goods and services related to health, leisure (such as musical instruments), and work (such as farming equipment), make their appearance in the pages of the periodicals. 
+ apologetics: Presenting the case for the faith and defending against challenges, whether those came from other religious writers or from broader cultural sources, such as the development of evolutionary science was a common feature in the religious periodicals of the day. These topics capture general language of debates and the particular case of science. Topics overlaps some with those categorized under "bible", "church_and_state", "health", and "theology."
+ bible: As a people of the book, references to the Bible are common throughout the Seventh-day Adventist periodicals. These topics capture quotations from the Bible.
+ church_and_state: One of the major issues linked to the end of time for Seventh-day Adventists was the threat of Sabbath legislation and other efforts to legislate religious practice, particularly Sunday observance. These topics capture the conversations around Sabbath legislation and more generally the defense of the separation of church and state.
+ community_news: The periodicals of the denomination served as a means of creating community among the dispersed members. These topics capture short reports on the activity of different regional conferences and their members.
+ conference_proceedings: Organizationally, the denomination used periodic conference meetings to conduct business. These were held at the local, regional, national, and international level and also took place for the different interest-focused "societies" within the denomination. These topics capture the formal language of the reported proceedings of these conferences, including discussions and votes on resolutions. 
+ correspondence: Letters to the editor also served an important function early on in the denomination's history as believers talked back to the publication and to each other about their beliefs and experiences. These topics capture the distinctive and shared rhetoric of the testimonials that were a frequent element of the early publications.
+ education: Particularly in the second half of this study, education becomes a key elements of the Seventh-day Adventist culture and evangelistic process. This included both Sabbath educational programs, which were focused on religious outreach and literacy, as well as the more formal educational opportunities of the Seventh-day Adventist colleges and medical training programs. 
+ EGWhite: Ellen White was a frequent contributor to  Seventh-day Adventist periodicals, both directly and through quotation. These topics predominantly capture pieces where Ellen White's voice can be distinctively heard.
+ eschatology: Eschatology, or the study of issues around the end of time, was a perennial concern for Seventh-day Adventists, as a religious group formed around particularly end-times beliefs. These topics capture theological and interpretive articles seeking to interpret the Bible on the issue of the second coming.
+ general_interest: At times more a source of curiosity than useful topics, the "General Interest" category includes listing of world news and natural disasters, descriptions of places, populations, and military culture from a number of different historical conflicts. 
+ health: Health was part of the religious and cultural practice of the early Seventh-day Adventists, and the subject of a number individual publications as well as a concern for general audiences. These topic capture discussions around various health topics, from treatments for particular illnesses (Tuberculosis) to more general discussions of habits, exercise, and disease.
+ history: History for Seventh-day Adventist authors provided the record used to prove their interpretations of the Bible (particularly Daniel and Revelations), as well as to show where humans stood in the unfolding of time. These topics trace various historical topics of interest, including the Reformation, the French Revolution, and the history of religious liberty.
+ meeting_reports: While various conference meetings provided the space for denominational leaders to come together and provide guidance for the denomination, not all were able to attend. As a results, descriptions of these events were published in the papers, helping extend that community both in space and time. These topics capture those descriptive reports.
+ missions: Outreach and missions became a significant aspect of Seventh-day Adventist culture and included both foreign missions as well as local missions in the form of health care and periodical and tract canvassing. All members were encouraged to participate as much as possible, and these topics capture descriptions of the missions work and calls to participate.
+ nature: With the physical world valued as God's creation, SDA writers often included descriptions of landscapes, animals, and plants as part of their pieces. The underlying theme of these topics is the celebration of nature as reflecting the perfection of God.
+ nutrition: Related to health, SDA authors were very concerned about food and nutrition as part of the religious life, with the "natural law" as described in Old Testament writings and reflected in nature providing the best way to health (and salvation). Recipes and commentary on the usefulness (or not) of particular foods is a feature of the topics captured in this theme.
+ obituaries: Notices of the death of community members and descriptions of their lives of faith form a significant part of a community connected through the pages of the periodicals. 
+ organization: From the publication of constitutions for local conferences and institutions to the printing records of the current giving practices of different churches and regions, the topics under this category capture the more bureaucratic aspects of the denomination as reflected in the periodicals.
+ periodicals: Lists of titles and sales information are captured in these topic. There is some overlap here with "Advertisements"
+ piety: Contributors to the SDA periodicals often included poems, stories, and other more "sentimental" literature describing their faith and Christian experience. Such language is captured in these topics.
+ politics: Similar to concerns about Sabbath laws, SDA writers were frequent commentators on politics and the US government, which was watched as the future antagonist in the approaching final conflict between Satan and the church. These topics capture additional political concerns of the SDA, including the roots of religious freedom and concern regarding war.
+ prophecy: Separate from discussions of Ellen White's prophetic gift (known as the Spirit of Prophecy), SDA writers were interested in the Biblical prophecies around end times and spent much time discussing and interpreting their meanings. These topics capture the formal exegesis of the main prophetic text of Daniel and Revelations.
+ religious_commentary: Related to theology proper, SDA authors also provided commentary on different aspects of religious life, as well as religious alternatives. These topics include commentary on the ministry, descriptions of death and heaven, as well as discussions of Spiritualism.
+ reports_on_the_cause: Connected to the missions work of the denomination, the periodicals often featured updates on the work, from the construction of new buildings to accounts of the various meetings held and conversions won. Under this category also included various tellings of the history of the SDA publishing work.
+ scan_errors: Despite multiple approaches to clean and minimize the presence of OCR errors in the model corpus, the realities of digitized historical texts makes some amount of errors in transcription inevitable. These topics capture errors, as well as some roman numeral use (often used with the inclusion of Bible verses.)
+ sermons: Appearing most often in the context of reports from meetings, the periodicals included printings of sermons given on these occasions, frequently on the topic of salvation and religious practices. These topics capture the patterns of sermons.
+ signs_of_the_times: In keeping with their anticipation of the second coming, SDA authors kept track of world events, both current and historical, that could be interpreted through the lens of prophecy. These "signs" include a range of things, from astronomical signs to social unrest and commentary on rampant "sin."
+ social_commentary: With some overlap with more formal "signs of the times," SDA authors provided commentary on what they saw to be aspects of the surrounding culture that might be of concern to the spiritual development of Seventh-day Adventists. These topics include discussions of marriage, of sport, of money and immigration, as well as vices.
+ spiritual_growth: The development of virtue and overcoming sins was a significant concern for SDA authors, as the behavior of members was seen as reflecting on the progress and truth of the cause. These topics capture calls for charity, for perseverance, for overcoming sin, and for developing virtuousness and industry as part of the Christian life.
+ stories: To illustrate the ideal Christian life, authors included a number of stories to teach moral lessons, to report on missionary activity, and to relate theological lessons. These topics capture the language of story.
+ theology: Engaging in theological arguments and parsing theological claims was part of the process by which SDA writers developed their distinctive beliefs and culture. These topics include formal discussions about salvation, conditional immortality, tithing, and the law.
+ theology_sabbath: Of particular interest to SDA writers was the Sabbath. I separated out the theological discussions about the Sabbath from the more because of the distinctiveness of this particular question.
+ transportation: Train travel was a major feature of the life of SDA members and the development of the denomination, as the primary means by which members traveled to conferences, to the sanitariums, and to travel to the dispersed community. 

### topic_words  
Top 20 words for each topic, as identified by the topic model.

### topic_prevalence_overall
Prevalence of the particular topic across all documents in the corpus. Computed by MALLET as part of the topic model.