import numpy as np 
import pandas as pd 
import streamlit as st
import pandas as pd

# set title
st.title("Customer Features and Behavior Analysis")
# part 1
with st.expander("1. Preprocessed Dataset Overview"):
    st.markdown("""
        ### Dataset Introduction
        The Consumer Behavior Dataset contains 4k pieces of specific information providing comprehensive insights into consumers' preferences, tendencies, and patterns during their shopping experiences. This dataset encompasses a diverse range of variables, including demographic information, purchase history, product preferences, shopping frequency and customer character Description. Analyzing this dataset will help us to better understand the mechanisms by which consumer characteristics and behaviors influence sales, and the number of sales.

        ### Data Preprocessing Steps
        The data processing flowchart is shown below:
        """)
    st.image("./pictures/pipeline1.png", caption="Data Process Pipeline", use_column_width=True)
    
# part 2
with st.expander("2. Customer Analysis"):
    st.markdown("""
               👋 Hi, there. Firstly, we will analyze customer's Behavior and features, including age, gender, payment method and loyalty. Let's go!
               
                👨‍💻 Understanding and analyzing consumer behavior and characteristics is essential for businesses to develop effective marketing strategies, improve customer satisfaction and increase sales. 
                By gaining a deeper understanding of these factors, companies can better position their products and services to meet the needs of different consumer groups.
                """)
    st.markdown("""
              #### Purchase Amount by Age Group
               """)
    st.image('./pictures/20.png', use_column_width=True)
    st.markdown("""               
                🔍This graph shows the purchasing power of consumers in different age groups. The purchasing power of those below 20 years old is weakest as they are less financially independent. The **20-30** year olds have one of the highest purchasing power, which may be mainly due to the fact that this group is younger, more focused on outward appearance, and has the **highest frequency of product changes**, as well as the fact that this group is financially independent. 
                
                🔍There is a small drop in comparison to the 30-40 year olds. The 40-50 year old group gradually picks up. The **50-60** year olds having the highest purchasing power, is one of the key customer groups, possibly reflecting a peak in career earnings or possibly a shift in spending to **higher quality or higher priced** items. However, the post 60+ group has seen a greater fall in the amount of money purchased.
                
                💡**Loyalty programmes** should be implemented for the 20-30 and 50-60 focus customer groups to encourage repeat purchases and to increase the LTV of customers.For the 60+ customer group, which has more disposable income and therefore a high potential for growth, products can be developed that specifically cater to the needs and preferences of this group, thus increasing the amount of money purchased by this group.""")
    st.markdown("""
              #### Purchase Number by Purchase Frequency within each Age Group
               """)
    st.image('./pictures/21.png', use_column_width=True)
    st.markdown("""
                🔍For one of the largest customer groups: the 20-30 year old customer group,'Bi-Weekly' is the most prominent shopping frequency, indicating a high overall frequency of consumption.It is the same as in the previous analysis: the **product life cycle** in this group is relatively short. For this customer group, the speed of product development can be increased, e.g., the speed of iteration of clothing styles can be increased in order to increase the repurchase rate.
                
                🔍Another larger customer group, the 50-60 year olds, has a more even distribution of purchasing frequency, so flexible inventory management is needed to adapt to various purchasing frequencies and ensure supply chain efficiency and responsiveness. In addition, the frequency of low-frequency buyers can be gradually increased by adding more touchpoints.
                
                🔍For the 60+ customer group, it can be seen that 'annuallly' and 'Quarterly' are the most prominent, indicating that the consumption frequency of this group is relatively low. They are more inclined to buy products with high quality and low replacement frequency. Therefore, this group can be targeted with high quality and high price products. At the same time explore whether there are ways to stimulate the frequency of purchase.
                """)
    st.markdown("""
              #### Purchase Amount by Gender
               """)
    st.image('./pictures/22.png', use_column_width=True)
    st.markdown("""
                🔍The pie chart displays the distribution of purchase amounts by gender, showing that 67.7% of the total purchase amount comes from male customers, while 32.3% comes from female customers.This could suggest that the products offered are more appealing to men or that men are spending more on average than women.

                💡The business may consider revisiting its marketing strategy to better target female customers and balance the distribution of spending between genders. This could involve analyzing product offerings, marketing messages, and channels to ensure they resonate with a female audience.
                """)
    
    st.markdown("""
              #### Payment Method Distribution
               """)
    st.image('./pictures/37.png', use_column_width=True)
    st.markdown("""
               🔍The pie chart displays a nearly uniform distribution of payment methods used for purchases, including Venmo, PayPal, Bank Transfer, Cash, Credit Card, and Debit Card. Credit Card payments have a slight edge at 17.8%, while the other methods range closely from 16.2% to 16.7%.

               💡The diverse use of payment methods suggests that customers appreciate a **variety of options** to complete their transactions. While credit cards lead marginally, the even distribution underscores the importance of offering **multiple payment options** to cater to different customer preferences. This flexibility could be a factor in customer satisfaction and could potentially influence purchase decisions. Businesses should ensure their payment processing systems are equipped to handle this variety efficiently.
                """)
    st.markdown("""
              #### Purchase Number by Agegroup and Payment Method
               """)
    st.image('./pictures/38.png', use_column_width=True)
    st.markdown("""
                🔍The stacked bar chart shows the number of purchases made by different age groups using various payment methods. There is an even distribution of payment methods among the different age groups. 
                
                🔍In the 60+ age group, the distribution of payment methods is also not predominantly in non-digital payment methods such as CASH, as I assumed, suggesting that senior customers have a large acceptance of the diversity of payment methods and do not need to be taken care of by special strategies.
                """)
    
    st.markdown("""
              #### Subscription Status Distribution
               """)
    st.image('./pictures/39.png', use_column_width=True)
    st.markdown("""
               🔍The pie chart displays the distribution of subscription status among customers, with 73% not subscribed and 27% holding a subscription.

               💡This distribution indicates a significant opportunity to **grow the subscription base**. Marketing efforts could focus on highlighting the benefits of subscription to the large segment of non-subscribers. Additionally, analyzing the reasons behind the choice not to subscribe could inform strategies to convert one-time buyers into subscribers, potentially increasing customer lifetime value and ensuring a steady revenue stream.
                """)
    st.markdown("""
              #### Gender and Age Distribution for Subscription
               """)
    st.image('./pictures/40.png', use_column_width=True)
    st.markdown("""
                🔍The pie charts represent the demographics of subscribers based on gender and age. The first chart shows that 100% of the subscribers are male, indicating that no female subscribers are present in the data set. The second chart shows a more balanced age distribution for subscriptions, with each age group from 20 years and above holding a relatively equal share of subscriptions, except for the under-20 age group, which has a significantly smaller portion.
                
                💡The exclusive male subscriber base suggests a significant untapped market among female customers that the business could target for subscription growth. The uniform age distribution among subscribers above 20 years indicates that the subscription offering resonates across a broad age range, potentially allowing for age-inclusive marketing strategies. 
                """)
    st.markdown("""
              #### Previous Purchases by Gender and Agegroup
               """)
    st.image('./pictures/41.png', use_column_width=True)
    st.markdown("""
                🔍The box plots display the distribution of previous purchases by customers, segmented by gender on the left and by age group on the right. Both genders have a similar median number of previous purchases, with males showing a slightly wider interquartile range. Regarding age groups, the distribution is fairly even across the board, with all age groups showing a similar median number of previous purchases, although the 50-60 age group has a slightly higher median.
                
                💡The data suggests that gender does not significantly influence the frequency of previous purchases, implying that both male and female customers are equally engaged in terms of buying frequency. The consistent number of purchases across age groups indicates that the customer base is diverse and that all age segments are active purchasers. The slightly higher median in the 50-60 age group may reflect greater brand loyalty or financial stability in this demographic. Marketing strategies should continue to be inclusive, targeting all age groups and genders.
                """)
    


# part 3
with st.expander("3. Product Category and Features"):
    st.markdown("""
               👋 In this section, we will analyse the impact of different product types and characteristics, such as color, size on the amount of sales. 
                From this, we will make recommendations on the production, inventory management and sales of the product.
                """)
    st.markdown("""
              #### Purchase Amount by Product Category
               """)
    st.image('./pictures/23.png', use_column_width=True)
    st.markdown("""
               🔍The chart illustrates the distribution of purchase amounts across different product categories. Clothing leads with the highest purchase amount, indicating a strong preference among consumers for this category. Accessories follow as the second-highest category, popular among customers, but with significantly lower purchase volumes compared to clothing. Footwear shows a moderate purchase amount, suggesting a smaller market share compared to clothing and accessories. Outerwear has the lowest purchase amount, potentially reflecting seasonal buying patterns, higher unit prices, or reduced consumer interest. 

               💡This figure suggests that companies should focus on clothing and accessories, optimizing inventory and allocating marketing resources accordingly. Given the lower sales volume of outerwear, market research might be needed to understand the underlying reasons and develop targeted marketing campaigns during peak seasons to boost sales. Meanwhile, considering the moderate sales volume of footwear, expanding this product line could be beneficial if it has higher profit margins or if there is an untapped market opportunity.
                """)
    st.markdown("""
              #### Purchase Amount by Specific Item
               """)
    st.image('./pictures/24.png', use_column_width=True)
    st.markdown("""
                🔍This bar chart details the purchase amount by specific items, displaying a range of products and their respective sales figures.The items are broadly distributed across the spectrum concerning purchase amounts. Blouses, dresses, and shirts appear to be the leading items in sales, whereas handbags, backpacks, and different types of jeans are on the lower end of the sales spectrum. This spread indicates a diverse product interest among consumers, with particular strength in the top-selling items which are staples in many wardrobes.
                
                🔍The dominance of blouses, dresses, and shirts suggests that focusing on these items could be profitable, ensuring that stock levels meet demand and that there are a variety of styles and sizes available. The lower sales figures for handbags and backpacks may indicate a need for a review of these lines—potentially looking at pricing, style selection, or marketing efforts. For the various types of jeans, considering their fashion staple status, it may be beneficial to investigate why they are lagging in sales; this could involve customer feedback, competitive analysis, and reviewing product placement and promotion.
                
                💡One point to note！！！
                
                ❓❓women's shirts and dresses and jewellery have the highest sales, but men's spending is much larger in the gender distribution of sales, which suggests that there is a possibility that **men may be contributing a significant portion of the sales when purchasing a gift for a woman**, which is especially common during special holidays or occasions. If this is indeed the consumption structure, the marketing strategy is quite different from what we have previously proposed to attract female consumers. 
                
                Next, we will analyse the gender ratio of purchases of women's shirts, dresses and jewellery:
                """)
    st.markdown("""
              #### Blouse and Dress Purchase Amount by Gender
               """)
    st.image('./pictures/25.png', use_column_width=True)
    st.markdown("""
                💡This pie chart validates our conjecture that most of the women's goods are paid for by men, and that's why men have the highest percentage of spending money. So based on this analysis, we propose several new marketing strategy below:
                
                **Gift Purchasing Options:** Offer easy-to-navigate gift purchasing options, including gift cards, gift wrapping services, and personalized recommendations.

                **Seasonal Marketing:** Launch special marketing campaigns targeting men who may buy gifts for women during key shopping holidays like Valentine's Day, Mother's Day, Christmas, etc.

                **Promotional Campaigns:** Implement couple-based promotions, such as "buy one, get one free" or "couples discounts," aimed at attracting both male and female customers.
                
                **Market Research:** Conduct customer research to understand the decision factors and preferences of male customers when purchasing products for women.
                """)
    st.markdown("""
              #### Purchase Amount by Agegroup within each Category
               """)
    st.image('./pictures/26.png', use_column_width=True)
    st.markdown("""
                🔍The provided bar chart depicts the purchase amount within each product category, broken down by age groups.For Accessories, The 30-30 age group appears to be the largest spender, with purchase amounts decreasing as the age increases,however the amounts increase suddenly in 60+ age group.For Clothing, This category shows the highest purchase amounts across all age groups, with the 50-60 age group leading, followed closely by the 20-30 age groups. For Footwear, The 50-60 age group spends more than other age groups clearly.For Outerwear, the 40-50 age group stands out as the highest spender.
                
                💡Marketing initiatives should be tailored according to age-specific preferences, with a focus on the 50-60 age groups for clothing and footwear, and on the 20-30 and 60+ age group for accessories.Outerwear's overall sales are low and it should focus on developing sales strategies that capitalize on the preferences of customers in the 40-50 age group to increase sales. 
                """)
    st.markdown("""
              #### Purchase Amount by Size within each Category
               """)   
    st.image('./pictures/27.png', use_column_width=True)
    st.markdown("""
                🔍The bar chart presents the purchase amounts categorized by product size within each product category.In every category, size M is the most popular, with much higher sales amounts than other sizes, then followed by Size L, S, and XL.

                💡Given the **popularity of sizes M and L** in clothing and footwear, it's essential to ensure that stock levels for these sizes are sufficient to meet demand. Tailor marketing efforts to highlight the availability of popular sizes, and consider special promotions for sizes with lower sales to increase turnover.
                """)
    st.markdown("""
              #### Purchase Amount by Product Color
               """)
    st.image('./pictures/28.png', use_column_width=True)
    st.markdown("""
                🔍The colors are almost uniformly distributed in terms of purchase amounts, with green slightly leading. This uniformity suggests that there is no single dominant color preference among consumers, which can indicate a diverse customer base with varied tastes. The close competition among the colors could also imply that consumers are purchasing items across a spectrum of colors rather than sticking to traditional favorites.

                💡Maintaining a wide variety of colors in the product lineup may continue to appeal to a broad customer base. Monitor color trends closely, as shifts in fashion and seasonal preferences can change the popularity of colors quickly. Balance inventory across the color spectrum to prevent overstocking of less popular colors and to ensure that popular colors are readily available.
                """)
    st.markdown("""
              #### Purchase Amount by Product Color in Seasons
               """)
    st.image('./pictures/29.png', use_column_width=True)
    st.markdown("""
                💡In the chart above, I have listed the top 5 colors in terms of sales and found that regardless of the season, it is the five colors 'black', 'Brown', 'Beige', 'Blue', 'Charcoal' that are the most popular, with the internal order varying from season to season. Stock management of colors can use this as a reference.
                """)

# part 4
with st.expander("4. Season Factors"):
    st.markdown("""
               👋 This part I focus on exploring if there is a seasonal trend in the sale of merchandise 
                so that I can decide whether or not to adjust my sales plan according to the seasons.
                """)
    st.markdown("""
              #### Purchase Amount by Season
               """)
    st.image('./pictures/31.png', use_column_width=True)
    st.markdown("""
               🔍The bar chart displays the purchase amounts by season, with each bar representing a different season of the year. The purchase amounts are fairly consistent across all seasons, with a slight variation. Fall shows the highest purchase amount, followed by Spring, Winter, and Summer, which has the lowest, yet still comparable, purchase amount.

               💡Plan inventory with a consistent supply throughout the year, with a slight increase before the Fall season to accommodate the peak.
                """)
    st.markdown("""
              #### Purchase Amount by Category within each Season
               """)
    st.image('./pictures/32.png', use_column_width=True)
    st.markdown("""
                🔍The bar chart details the purchase amount by frequency category within each season. All seasons display a similar distribution pattern across the different purchase frequencies, with no single category or season showing a dramatically higher purchase amount than others. 

                💡The uniformity across seasons and purchase frequencies suggests that customers have a **steady purchasing habit** that does not significantly change with seasons.Marketing efforts can be consistently applied throughout the year. However, subtle seasonal marketing could still be beneficial to cater to any slight variations.For example, the shopping frequency in Fall has more 'Annually', which means lower frequency.
                """)
# part 5
with st.expander("5. Rating"):
    st.markdown("""
               👋 In this part, I will analyse customer ratings of the product.
               
                👨‍💻 Customer ratings are critical as they serve as direct indicators of consumer satisfaction, 
                reflecting the market acceptance and quality of a product. High ratings and a large volume of reviews typically signify greater customer trust and satisfaction, 
                which can attract more potential buyers and also provide valuable feedback for businesses to improve their products and customer service.
                """)
    st.markdown("""
              #### Product Rating Distribution
               """)
    st.image('./pictures/33.png', use_column_width=True)
    st.markdown("""
               🔍The bar chart illustrates the distribution of product ratings, showing the count of products within each rating category. Products rated 3-4 have the highest count, closely followed by those rated 4-5. There are fewer products with ratings of 2-3 and significantly fewer with a rating below 2. This indicates that the majority of products have favorable ratings from customers.

               💡The presence of products in the 2-3 rating range, while fewer, points to **potential areas for improvement**. Understanding why these products are rated lower and addressing those issues could improve customer satisfaction and sales.
                """)
    st.markdown("""
              #### Rating Distribution for Clothing, Accessories, Footwear, Outerwear
               """)
    st.image('./pictures/34.png', use_column_width=True)
    st.markdown("""
                💡The pie charts represent customer ratings distribution across four categories.Clothing and Outwear have similar profiles with over a fifth of products falling into the 2-3 rating range, indicating potential quality issues. In contrast, Accessories and Footwear have a higher proportion of products with 4-5 ratings, showing greater customer satisfaction.For products with ratings falling in the 2-3 range, focus on verifying the reasons for the low ratings.
                """)
# part 6
with st.expander("6. Discount and Promotion"):
    st.markdown("""
               👋 In this part, I want to explore whether discounts have a positive effect on product ratings and the number of sales, which determines the designation of sales strategies.
                """)
    st.markdown("""
              #### Review Rating by Discount and Promo Code Used
               """)
    st.image('./pictures/35.png', use_column_width=True)
    st.markdown("""
               🔍The box plots compare review ratings based on whether a discount or promo code was used. Both discounts and promo codes appear to have a median review rating of around 4.0. The interquartile ranges are similar regardless of the discount or promo code usage, suggesting that pricing incentives do not significantly affect the median customer satisfaction.

               💡The data suggests that while **discounts and promo codes do not drastically alter the average customer satisfaction**, they also do not detract from it. This implies that such pricing strategies could be employed without risking a decrease in perceived product quality or customer satisfaction. 
                They may be effective tools for increasing sales volume or attracting new customers without negatively impacting brand reputation. 
                However, specific probability calculations are still required to determine whether it is cost-effective to maintain the discount.
                """)
    st.markdown("""
              #### Purchase Number by Discount Applied and Promo Code Used
               """)
    st.image('./pictures/36.png', use_column_width=True)
    st.markdown("""
                🔍The bar charts compare the number of purchases made with and without discounts and promo codes. Purchases without discounts are higher than those with discounts. Similarly, the number of purchases made without the use of a promo code slightly exceeds the number made with a promo code.
                
                💡The similar purchase numbers probably suggest that while discounts and promo codes do incentivize some buyers, they are not the sole driving factor for a majority of purchases. 
                However, it is also possible that the **lower number of purchases was simply due to the company itself offering fewer opportunities for discounts and opportunities to use coupon codes.** Further confirmation of the causal relationship is needed.
                """)
   
with st.expander("7. Location"):
    st.markdown("""
                👋In this section I focus on analyzing the regional distribution of sales and ranking the sales in specific states. This analysis provides a reference for the company's geographic expansion strategy.
                #### Sales Activity Location
                """)

    st.markdown("""#### HeatMap of Purchase Amount Distribution""")
    st.image('./pictures/42.png', use_column_width=True)
    
    st.markdown("""
        🔍The heat map shows concentrated sales activity in the Northeastern United States, particularly around the New York area, indicated by the red and orange colors that signify higher sales volumes.The West Coast, particularly in California, and the Southern states show moderate to high levels of activity, with the intensity decreasing as it moves inland.There are isolated areas of activity, potentially major cities, that stand out in Alaska and Hawaii, indicating significant market engagement in these locales.

        💡The high levels of activity in the **Northeast and along the West Coast** could be further capitalized on with focused marketing campaigns, potentially increasing the customer base in these economically vibrant regions.The isolated hotspots could represent areas where market presence is strong but could benefit from expansion efforts or increased marketing to grow the customer base.The low activity in central North America suggests either an untapped market potential or a need for increased brand awareness and penetration efforts.
                """)
    st.markdown("""#### Top 10 Purchase Amount by Location""")
    st.image('./pictures/30.png', use_column_width=True)
    st.markdown("""
               💡The bar chart lists the top 10 locations by purchase amount, with California leading, followed by Alabama, Alaska, and others. The purchase amounts are relatively close in value, suggesting a competitive market across these top-performing states.
                """)

# part 8
with st.expander("8. Summary and Suggestion"):
    st.markdown("""
               👋This project entailed a systematic analysis of a retail company's customer data, captured in the "shopping_trends.csv" file. The process began with data preprocessing, including the removal of duplicates and missing values. The data visualization step involved creating various charts to depict customer demographics, purchase behavior, and preferences related to payment methods, discounts, and subscriptions.
               
                👨‍💻The visualizations covered a range of indicators including customer age and gender, product categories, color, and size, along with purchase-related data such as location, seasonality, ratings, discounts, and loyalty aspects like subscription status and history of previous purchases. The project concluded with a multi-indicator mixed analysis to draw comprehensive insights from the cross-referencing of these diverse data points.
                
                **💡Suggestion:**

                **Customer Segmentation:** Focus marketing efforts on the most active age groups (20-40 years) while devising strategies to engage the under-20 and 60+ demographics more effectively.

                **Customer Gender:** Watch out for men buying for women and develop special strategies such as Gift Purchasing to target this behavior.

                **Loyalty Programs:** Given the uniformity in purchase frequency, develop or enhance loyalty programs to retain and grow the existing customer base, specifically targeting the male demographic which exclusively holds subscriptions.

                **Product Quality and Satisfaction:** Address the lower ratings in the Clothing and Footwear categories with quality improvements and utilize the higher satisfaction in Accessories and Outerwear in marketing strategies.

                **Payment Flexibility:** Maintain a variety of payment options to cater to all customer preferences, ensuring an efficient and user-friendly payment system.

                **Gender Inclusivity in Subscriptions:** Investigate why there are no female subscribers and develop targeted subscription offerings that appeal to female customers.

                **Seasonal Inventory Management:** Align stock levels with the consistent demand shown throughout the year, with an emphasis on the Fall season.

                **Promotions and Discounts:** Utilize discounts and promo codes strategically to boost sales volumes without affecting customer satisfaction or the perceived value of the products.

                **Use of Data Analytics:** Continue to employ data analytics for deeper insights into customer behavior and preferences, enabling data-driven decision-making for product development, marketing, and customer service improvements.
                """)    

