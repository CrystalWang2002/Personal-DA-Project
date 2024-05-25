import streamlit as st
import function as func

# set title
st.title("Amazon Sales Analysis and Recomendation System")

# part 1
with st.expander("1. Preprocessed Dataset Overview"):
    st.markdown("""
        ### Dataset Introduction
        In this project, I will analyze Amazon Sales Dataset. This dataset contains 1k+ pieces of specific information about Amazon products with product ids, prices, discounts, categories, customer reviews and other important details. Analyzing this Dataset will provide in-depth insights into market trends, consumer behavior, pricing strategies, and product performance to support more effective business decisions.
        ### Data Preprocessing Steps
        The following steps were taken to preprocess the dataset:

        - **Data Type Changes**: Converts variables such as price, percentage and rating from object type to numeric type. 
                If the variable is a mixture of numbers and units, we can first convert the variable to a string type, 
                delete the unit character and then convert it to a numeric type.
        - **Missing Value Handling**: Check and Drop rows with missing values.
        - **Create product Information Table**: Extract the columns related to product information from the table and construct a new table. 
                Extract main category and sub-category from 'category' variable respectively as new variables.
                Calculate the discount amount and percentage using actual_price and discount_price.
        - **Data Visualization and Analysis**: Visualize data such as product sales quantity, discounts, customer ratings and reviews, 
                analyze and evaluate the results of the visualizations.
        
        The data processing flowchart is shown below:
        """)
    st.image("./pictures/pipeline.png", caption="Data Process Pipeline", use_column_width=True)

# part 2
with st.expander("2. Most Popular Product by Category"):
    st.markdown("""
            👋 Hi,there! Firstly, I will compare the number of products in different categories and observe which products are most popular among consumers, 
                so that company can adjust its marketing strategy according to consumer preferences.
             """)
    st.image("./pictures/1.png", caption="Most Products by Category", use_column_width=True)
    st.markdown("""
            🔍The first chart lists five main categories, Electronics category has the highest number of products (526), followed by Computers & Accessories (451), and Home & Kitchen (448). In contrast, the number of products in musical instruments and other lower-ranked categories was small (less than 2).

            🔍The second chart shows more specific subcategories. Accessories & Peripherals have the highest number of products (379), followed by Kitchen & Home Appliances (308).
            In Contrast, Networking Devices, Office Paper Products, External Devices & Data Storage category and other lower-ranked categories has little number of products (less than 34).

            💡For both main and subcategories, The higher quantities indicate these may be categories with **the highest customer demand**. Inventory should be managed accordingly to ensure a sufficient supply of products in these popular categories.what's more, high quantities might indicate high consumer interest or market saturation. Further data is needed to assess the growth potential and competitive landscape of these categories.

            💡For categories with lower quantities, Explore whether the low sales are due to product quality or marketing strategy. If the product sales do not increase significantly after improving quality and promotion, and the product is not a high-margin product, it might be worth assessing **whether to continue investing** in it.
                """)
# part 3
with st.expander("3. Product Discount"):
    st.markdown("""
               👋 Hi, Next I will analyse the discounts on different categories of goods. 
               
                👨‍💻 Analyzing product discounts is essential for optimizing sales strategies, managing profits and costs, understanding customer behavior, responding to competition, 
                and balancing inventory with long-term brand health. This analysis helps companies align market strategies and promotions to boost short-term sales and sustain long-term brand loyalty and growth.
                """)
    st.markdown("""
              #### Expensive Product After Discount
               """)
    st.image('./pictures/2.png', use_column_width=True)
    st.markdown("""
               🔍The bar chart details the Top 5 Expensive Products After Discount on Amazon, it appears that even after discounts, the Sony Bravia 164 cm is the most expensive, suggesting a **strong brand positioning** that allows it to maintain a premium price. 
                The descending order of pricing indicates a **competitive market** for high-end TVs, with the OnePlus 163.8 cm and VU 164 cm following, which shows a diverse range in consumer choice for luxury smart TVs. 

               💡This information could suggest that while discounts are an effective way to attract consumers, premium brands like Sony can still command higher prices due to perceived quality or brand loyalty. Therefore, for retailers and manufacturers, maintaining a **balance between price competitiveness and brand value** is crucial, and for Amazon, this variety in pricing strategies highlights its role as a comprehensive marketplace catering to different segments of consumers.
                """)
    st.markdown("""
              #### Cheap Product After Discount
               """)
    st.image('./pictures/3.png', use_column_width=True)
    st.markdown("""
                🔍The bar chart displaying the Top 5 Cheapest Products After Discount on Amazon indicates that small electronics and office supplies, such as the GIZGA essentials keyboard protector and Classmate Octane Neon gel pens, have the lowest prices post-discount. This suggests that Amazon caters to **budget-conscious consumers** by offering substantial discounts on everyday items, likely driving volume sales. The presence of items like USB LED lights and data cables further implies that there's a targeted strategy to attract customers seeking practical, low-cost tech accessories. 

                💡For businesses, this could indicate the importance of competitive pricing in the lower-end market to remain relevant on platforms like Amazon, while for consumers, it highlights Amazon's role as a destination for affordable purchases across diverse categories.
                """)
    st.markdown("""
              #### Discount Quantity
               """)
    st.image('./pictures/4.png', use_column_width=True)
    st.markdown("""
                🔍The bar chart on the Top 5 Products with the Largest Discount on Amazon reveals that high-ticket items like the Sony Bravia TV and Coway Air Purifier are receiving the most substantial price reductions. This suggests a strategy to **move high-value inventory**, possibly to make room for new models or to meet sales targets. These large discounts on premium products may also indicate a focus on attracting deal-seeking, high-end consumers or leveraging discounts to drive purchases of products with higher margins. 

                💡From a business perspective, this can be seen as an approach to stimulate sales in higher-priced categories by offering significant value to customers, which could boost overall sales volume and customer acquisition in these segments.
                """)
    st.markdown("""
              #### Discount Percentage by Category
               """)
    st.image('./pictures/5.png', use_column_width=True)
    st.markdown("""
                📊The bar graph illustrates that the Home Improvement category has the highest average discount percentage on Amazon, closely followed by Computers & Accessories, and Health & Personal Care. This indicates that Amazon might be targeting consumers looking to invest in home projects and tech gear, possibly reflecting a response to **market trends or excess inventory** in these categories. Meanwhile, Office Products and Toys & Games receive notably lower discounts, which could suggest a smaller margin or less need to incentivize sales in these categories. 
                """)
   
    st.image('./pictures/6.png', use_column_width=True)
    st.markdown("""
                📊The bar chart indicates that Wearable Technology receives the highest discount percentages within Amazon's subcategories, suggesting a strategic push to increase sales in a fast-growing tech sector. High discounts on items in the Kitchen & Dining and Headphones, Earbuds & Accessories categories could be intended to attract consumers looking to upgrade their home and personal electronics, reflecting consumer trends or overstock. In contrast, Home Storage & Organization has the lowest discount rate, which might indicate **steady demand**without the need for aggressive price reductions. 
                """)
    st.markdown("""
              #### Discount Percentage Distribution
               """)
    st.image('./pictures/7.png', use_column_width=True)
    st.markdown("""
                🔍The histogram showcases a distribution of discount percentages, with a concentration of products falling in the **middle range** and a normal-like distribution **skewed slightly right**.This suggests most Amazon discounts are moderate, with fewer products having very low or very high discounts. 
                
                💡This distribution could imply a balanced approach to discounting, 
                likely designed to appeal to a broad customer base without significantly diminishing profit margins. It indicates a strategic use of discounts to drive sales across a range of products while avoiding the pitfalls of deep discounting that could devalue product perception or hurt profitability.
                """)
    

# part 4
with st.expander("4. Product Ratings"):
    st.markdown("""
        👋In this part, I will analyse customer ratings of the product. 
                
        👨‍💻Customer ratings and the number of reviews are critical as they serve as direct indicators of consumer satisfaction, reflecting the market acceptance and quality of a product. High ratings and a large volume of reviews typically signify greater customer trust and satisfaction, which can attract more potential buyers and also provide valuable feedback for businesses to improve their products and customer service. 
        """)
    st.markdown("""
        #### Ratings Distribution 
        """)
    st.image('./pictures/8.png', use_column_width=True)
    st.markdown("""
        🔍The graphs depict the distribution of product ratings and the distribution of the number of ratings. The first graph shows a normal distribution of ratings skewed towards higher values, indicating that most products receive **good** ratings, with few products rated poorly. The second graph reveals that a large number of products have very **few** ratings, with rapidly diminishing counts as the number of ratings increases, suggesting that only a few products have a very high number of ratings. 

        💡This data could be interpreted as a sign that while customer satisfaction tends to be high, widespread engagement in the review process is limited to a smaller subset of products. It highlights the importance of not only achieving high ratings but also encouraging a higher volume of customer feedback to enhance **product credibility** and consumer trust.
                """)
    st.markdown("""#### Rating Distribution by Category""")
    st.image('./pictures/9.png', use_column_width=True)
    st.markdown("""
               This box plot illustrates the distribution of ratings across various main product categories.
                
                Categories like "Office Products","Home Improvement" and "Toys & Games" generally have high median ratings, close to 4.25 or above, indicating customer **satisfaction**.

                "Electronics" has the widest interquartile range (IQR), suggesting a significant variation in customer satisfaction within this category. Wide IQRs can indicate a diverse customer base with **varying expectations**. Understanding the segments within these subcategories could help tailor products more closely to customer needs.

                Outliers are present in several categories, such as "Home & Kitchen" and "Electronics", which can indicate a few products with ratings significantly lower than the general trend.There should be a focus on whether these outliers are **malicious reviews or customers' real product experience**.
                """)
    st.image('./pictures/10.png', use_column_width=True)
    st.markdown("""
                This box plot illustrates the distribution of ratings across various sub product categories.

                The "Craft Materials","Office Electronics" and "Components" subcategories show a tight distribution with a higher median rating, which suggests consistent customer **satisfaction**.

                "Headphones,Earbuds & Accessories","Microphones" and "Car Accessories" have the lower median ratings(below 4.0 rating), which could be a concern that needs **quality reviews and customer feedback analysis** to identify and rectify issues.

                "Printer, Inks & Accessories" show a wide spread in ratings (IQR), pointing to a varied customer experience. This could reflect a mix of premium and budget products within these subcategories, Or it may reflect the fact that customer requirements vary widely and products need to be **more customized**.

                Some categories like "Kitchen & HomeApplicances","Heating, Cooling & AirQuality" and "Wearable Technology" have a number of outliers on the left, We need to investigate whether these outliers are due to error logging or because customers are having a very poor experience with the product.
                """)
# part 5
with st.expander("5. Product Reviews"):
    st.markdown("""
       ☁️In this section, we will observe customers' written reviews of products and analyse whether their attitude towards products is positive or not.
        """)
    st.markdown("""
        #### Wordcloud 
        """)
    st.image('./pictures/11.png', use_column_width=True)
    st.markdown("""
                **From the word cloud, we can discern several prominent words which suggest key themes:**

                **"Quality" and "Good":** These words are quite prominent, suggesting that overall, the sentiments in the data are positive regarding the quality of the product or service being reviewed.

                **"Phone" and "Sound":** The prominence of these words might indicate that the data includes reviews or discussions about a smartphone or audio-related product.

                **"Price" and "Value":** This suggests that price and value for money are significant considerations for the individuals whose opinions are represented.

                **"Issue":** This word's presence indicates that there are some concerns or problems being discussed, though it's not as dominant as positive words.

                **"Easy":** Ease of use or the user experience seems to be a positive aspect of the product or service.
                """)
    st.markdown("""
       **Then I generated a Wordcloud from customer feedback for products with higher ratings (greater than 4). It shown as follows:**
        """)
    st.markdown("""
        #### Wordcloud (Rating >= 4)
        """)
    st.image('./pictures/12.png', use_column_width=True)
    st.markdown("""
                **From the word cloud, we can discern several prominent words which suggest key themes:**

                **Product Quality:** Words like "quality," "best," "great," and "good" are quite prominent, suggesting that the overall product quality is highly regarded.

                **Ease of Use:** The word "easy" stands out, which implies that the user experience is straightforward and user-friendly.

                **Device Performance:** The presence of words such as "fast," "speed," and "performance" indicates that customers are satisfied with the operational aspects of the products.

                **Product Categories:** The words "phone," "TV," "laptop," and "cable" suggest the types of products being reviewed. The positive sentiment around these categories implies that they are well-received.

                **Use Cases:** "Work," "using," "watch," and "screen" suggest that the products are used for a variety of functions, from entertainment to work-related activities.

                **potential problem:** While "Issue" and "problem" are smaller, indicating fewer mentions, they're still present, which means some customers have had less-than-ideal experiences.
                """)
# part 6
with st.expander("6. Correlation Analysis"):
    st.markdown("""
       Finally, I will conduct a correlation analysis of the important indicators mentioned above, so as to provide reference for the formulation of market strategies.
        """)
    st.markdown("""
        #### Heatmap 
        """)
    st.image('./pictures/13.png', use_column_width=True)
    st.markdown("""
                **The image appears to be a heatmap representing the correlation between various variables associated with product pricing and customer ratings. Here's an analysis based on the correlation coefficients shown:**

                **Actual Price vs. Discounted Price:** With a correlation of 0.96, this indicates a very high positive correlation, suggesting that as the actual price increases, the discounted price also increases proportionally. This is expected as discounts are often a percentage of the actual price.

                **Rating Count vs. All Pricing Variables:** All correlations are very weak (ranging from -0.036 to 0.012), suggesting that the number of ratings a product receives is not strongly influenced by its price or the discount applied.

                The lack of a strong correlation between price and ratings indicates that customers **do not necessarily rate products based on how expensive they are or how much discount they receive**. Instead, other factors like quality, brand perception, and customer satisfaction are likely more influential on ratings.

                To improve ratings, Marketers and sales teams should focus on enhancing the **intrinsic value** of the product, such as quality improvements or feature enhancements, rather than only relying on discounting strategies. what's more, company can take some steps to encourage customer reviews through other means, such as providing excellent customer service, follow-up emails after purchase, or incentives for providing feedback.
                """)
# part 7
with st.expander("7. EDA insights"):
    st.markdown("""
            📚**In summary,I focused on product pricing, customer satisfaction, market trends, and category demands.Specifically:**

            **Pricing Strategy:** By analyzing discount and pricing data, businesses can better understand how to price products to attract customers while maintaining profit margins.

            **Customer Satisfaction:** The analysis of ratings and review counts reveals which products and services are most favored by customers and which need improvement, helping businesses to optimize their product lines and service quality.

            **Market Trends:** Analysis of product category distributions shows which categories are most popular, aiding businesses in identifying opportunities for growth or adjustments needed in their market strategy.

            **Inventory and Supply Chain Management:** Understanding which product categories are most popular and have the largest discounts can help businesses better manage inventory and meet customer needs.

            **Consumer Behavior:** Keyword and correlation analysis provide in-depth understanding of consumer preferences and behavior, allowing businesses to tailor their marketing messages and improve product features.

            ✨**Based on the previous graphical analyses, here are some detailed development suggestions for Amazon:**
                
            **Differentiated Competition:** Given the abundance and generally high ratings of products in electronics and home appliances, Amazon could collaborate with manufacturers to develop exclusive products or bundles, further differentiating its offerings in these saturated markets.
                
            **Dynamic Pricing Strategy:** With high-value items maintaining high price points even post-discount, Amazon should consider implementing a more dynamic pricing mechanism that adjusts prices and discounts in real-time based on market demand and inventory levels.
                
            **Enhanced Customer Feedback:** To increase the number of reviews and customer engagement, Amazon could offer small discounts or reward points to customers who leave valuable feedback, thereby encouraging more reviews.
            
            **Inventory Management:** For categories with a wide range of products but varied sales, Amazon should leverage advanced data analytics to optimize inventory, reducing overstock of slow-moving items while increasing stock for popular, well-rated products.
            
            **Focus on Customer Experience:** Key phrase analysis suggests Amazon should emphasize factors like "quality," "ease of use," and "value for money" in product descriptions, recommendations, and search algorithms to enhance the purchasing experience.
            
            **Strategic Discounts and Promotions:** Amazon could apply strategic discounts during specific periods (like holiday seasons) for products with high ratings but fewer reviews to increase sales and product visibility.
            
            **Data-Driven Marketing:** Amazon should use textual analysis of customer ratings and reviews to gain insights into market trends and adjust its marketing strategies accordingly, such as highlighting product features that customers care about in promotions.
             """)

# part 8
with st.expander("8. Recommendation System"):
    df = func.load_data()
    user_id_encoded = st.text_input("Type in the User ID you want to give recommendation (ID range:0-1191)")
    top_n = st.text_input("Type in the number of recommend items you want to give:")
    if st.button("Recommend"):
        st.write(func.recommend_products(df, int(user_id_encoded), int(top_n)))

    
