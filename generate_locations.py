#!/usr/bin/env python3
"""Generate location pages for getnextlevel.marketing"""

import os

locations = {
    "Loudoun County, VA": {
        "Leesburg": {"state": "VA", "desc": "the county seat of Loudoun County, Leesburg blends historic charm with a thriving business community along King Street and the surrounding downtown district. From local shops in the Historic District to growing enterprises near the Leesburg Premium Outlets, businesses here compete for visibility in one of Northern Virginia's most visited towns.", "benefits": ["Rank higher in local search results across Leesburg and eastern Loudoun County", "Build a consistent content strategy that highlights your expertise to Leesburg residents", "Automate review collection from satisfied customers visiting your King Street location", "Grow your social media presence to reach families and professionals in the Leesburg area"]},
        "Ashburn": {"state": "VA", "desc": "known as Data Center Alley and home to a booming tech corridor along Route 7 and Loudoun County Parkway, Ashburn is one of the fastest growing communities in Virginia. With major developments like One Loudoun and Ashburn Village, local businesses face intense competition for the attention of tech professionals and young families.", "benefits": ["Dominate local search results for your industry across the Ashburn and Broadlands area", "Create targeted content that resonates with Ashburn's tech savvy, affluent customer base", "Build a five star review profile that stands out near One Loudoun and Ashburn Village", "Run social media campaigns that connect with the rapidly growing Ashburn community"]},
        "Sterling": {"state": "VA", "desc": "a bustling commercial hub along Route 7 and the Dulles Greenway corridor, Sterling serves as a gateway to Dulles International Airport. With shopping centers like Sterling Park and Cascades Marketplace, businesses here need strong digital presence to capture both local residents and the steady flow of travelers and commuters.", "benefits": ["Improve your Google rankings to capture customers searching near Dulles Airport and Route 7", "Publish SEO optimized content that targets Sterling and the surrounding Cascades community", "Generate more online reviews from your Sterling area customers automatically", "Maintain an active social media presence that reaches Sterling's diverse population"]},
        "Purcellville": {"state": "VA", "desc": "nestled in western Loudoun County at the foot of the Blue Ridge Mountains, Purcellville maintains a small town feel with a growing business scene along Main Street and 21st Street. The town serves as a hub for the surrounding wine country and rural communities, offering unique opportunities for businesses that know how to market locally.", "benefits": ["Get found online by customers exploring Purcellville and western Loudoun wine country", "Create blog content that positions your business as a trusted local resource", "Collect reviews that build your reputation among Purcellville's tight knit community", "Use social media to connect with residents and visitors drawn to the Blue Ridge foothills"]},
        "Middleburg": {"state": "VA", "desc": "a charming village in the heart of Virginia hunt country, Middleburg is known for its equestrian heritage, boutique shops along Washington Street, and the renowned Salamander Resort. Despite its small size, businesses in Middleburg cater to an affluent clientele and a steady stream of tourists from the greater DC metro area.", "benefits": ["Attract high value customers searching for premium services in Middleburg and hunt country", "Develop refined content that matches Middleburg's upscale brand and equestrian culture", "Build a stellar review profile that appeals to discerning visitors and local residents", "Craft social media content showcasing your connection to Middleburg's distinctive community"]},
        "South Riding": {"state": "VA", "desc": "a master planned community in southeastern Loudoun County, South Riding is home to thousands of families who value convenience and quality. With its own town center, parks, and proximity to Route 50 and the Dulles Greenway, businesses serving South Riding need digital marketing that speaks to busy suburban families.", "benefits": ["Rank for local searches from South Riding families looking for nearby services", "Create helpful content that addresses the needs of South Riding's family oriented community", "Automate review requests to build trust with South Riding homeowners", "Engage South Riding residents on social media with content tailored to suburban life"]},
        "Brambleton": {"state": "VA", "desc": "one of Loudoun County's newest and fastest growing communities, Brambleton features the Brambleton Town Center with shops, restaurants, and entertainment. The community attracts young professionals and families who expect modern, digital first experiences from the businesses they support.", "benefits": ["Show up in search results when Brambleton residents look for local services online", "Produce fresh content that connects with Brambleton's young, digitally engaged audience", "Grow your review count with automated follow ups after every customer interaction", "Build brand awareness on social media across the Brambleton Town Center community"]},
        "Aldie": {"state": "VA", "desc": "located at the crossroads of Route 50 and the John Mosby Highway, Aldie sits between Loudoun's rural west and suburban east. With nearby vineyards, the historic Aldie Mill, and growing residential developments, businesses here serve a unique mix of longtime residents and newcomers to the area.", "benefits": ["Capture search traffic from customers in Aldie and along the Route 50 corridor", "Write content that highlights your local roots in the Aldie and Lenah area", "Earn more reviews from customers who value your connection to this historic community", "Share your story on social media to reach both longtime and new Aldie residents"]},
        "Lovettsville": {"state": "VA", "desc": "a small but growing town in the northernmost corner of Loudoun County, Lovettsville is known for its German heritage, the annual Oktoberfest celebration, and a welcoming community feel. Businesses here benefit from a loyal customer base and increasing interest from people relocating to this quieter part of Loudoun.", "benefits": ["Get discovered online by residents and newcomers exploring northern Loudoun County", "Create content that celebrates Lovettsville's unique heritage and community spirit", "Build a strong review profile that reflects the trust your Lovettsville customers have in you", "Use social media to connect with the growing Lovettsville and Brunswick area community"]},
        "Hamilton": {"state": "VA", "desc": "a quiet village between Leesburg and Purcellville, Hamilton offers a peaceful small town atmosphere with scenic views of the Blue Ridge. While small, businesses serving Hamilton benefit from their connection to the surrounding Loudoun County communities and the steady growth in the region.", "benefits": ["Appear in search results for customers between Leesburg and Purcellville", "Develop content that highlights your service to the Hamilton and western Loudoun area", "Collect genuine reviews from your loyal Hamilton area customer base", "Stay visible on social media to the growing communities around Hamilton"]},
        "Round Hill": {"state": "VA", "desc": "perched near the Blue Ridge in western Loudoun County, Round Hill is a small town with big community spirit. Close to hiking trails, wineries, and the scenic countryside, businesses here serve both residents and the outdoor enthusiasts who frequent the area.", "benefits": ["Rank in local search for customers in Round Hill and the Blue Ridge foothills", "Publish content that connects your business to Round Hill's outdoor lifestyle", "Generate reviews from satisfied customers in this close knit western Loudoun town", "Engage Round Hill residents on social media with authentic, community focused posts"]},
        "Lansdowne": {"state": "VA", "desc": "an upscale community in eastern Loudoun County near the Potomac River, Lansdowne is anchored by the Lansdowne Resort and surrounding residential neighborhoods. With proximity to Leesburg and the Dulles corridor, businesses serving Lansdowne have access to affluent professionals and families.", "benefits": ["Target local searches from Lansdowne residents and resort visitors", "Create polished content that matches the expectations of Lansdowne's professional community", "Build a premium review profile that attracts Lansdowne's discerning customer base", "Grow your social media following among Lansdowne and Riverside area professionals"]},
    },
    "Fairfax County, VA": {
        "Fairfax": {"state": "VA", "desc": "the independent City of Fairfax and surrounding Fairfax County areas form the heart of Northern Virginia's suburban landscape. Home to George Mason University, the historic Old Town Fairfax district, and major employers along the I-66 corridor, businesses here compete in one of the most educated and affluent markets in the country.", "benefits": ["Outrank competitors in one of Virginia's most competitive local search markets", "Produce expert level content that resonates with Fairfax's highly educated consumer base", "Build an impressive review portfolio that sets you apart near Old Town Fairfax and GMU", "Launch social media campaigns reaching the diverse professionals in the Fairfax area"]},
        "Reston": {"state": "VA", "desc": "a pioneering planned community built around Reston Town Center, Lake Anne, and miles of wooded paths, Reston combines urban amenities with a nature forward lifestyle. With the Silver Line Metro now connecting Reston to DC, local businesses face growing competition and opportunity in equal measure.", "benefits": ["Capture search traffic from Reston Town Center visitors and Metro commuters", "Create lifestyle driven content that appeals to Reston's active, community minded residents", "Earn five star reviews that boost your visibility near Reston Town Center and Lake Anne", "Build social media presence that reaches Reston's professional and family oriented audience"]},
        "Herndon": {"state": "VA", "desc": "a town with deep roots and a revitalized downtown along Elden Street, Herndon has transformed with the arrival of the Silver Line Metro. Situated near the Dulles Technology Corridor, businesses here serve a mix of longtime residents and the tech professionals drawn to the area's innovation economy.", "benefits": ["Rank higher for local searches in Herndon and the Dulles Technology Corridor", "Develop content that connects with Herndon's blend of historic charm and tech culture", "Automate review collection from customers near downtown Herndon and Innovation Station", "Grow your social media audience across Herndon's diverse and growing community"]},
        "Vienna": {"state": "VA", "desc": "a charming town known for its walkable downtown along Maple Avenue, the Vienna Farmers Market, and excellent schools, Vienna attracts families and professionals who value quality of life. Businesses on Maple Avenue and Church Street compete for the loyalty of this engaged, community oriented customer base.", "benefits": ["Show up first when Vienna residents search for services along Maple Avenue and beyond", "Write compelling content that speaks to Vienna's family focused, quality conscious community", "Generate more reviews from your Vienna customers with automated follow up sequences", "Connect with Vienna families and professionals through targeted social media content"]},
        "McLean": {"state": "VA", "desc": "one of the wealthiest communities in the United States, McLean is home to diplomats, executives, and government leaders. With upscale shopping at Tysons Galleria nearby and a strong local business scene along Chain Bridge Road, marketing to McLean requires a polished, professional approach.", "benefits": ["Position your business for premium searches in McLean and the Chain Bridge Road corridor", "Create sophisticated content that meets the expectations of McLean's affluent residents", "Build an exceptional review profile that reflects the high standards of McLean clientele", "Develop a refined social media presence worthy of one of America's premier communities"]},
        "Tysons": {"state": "VA", "desc": "rapidly transforming from a suburban office park into an urban downtown, Tysons is home to Tysons Corner Center, Tysons Galleria, and a growing skyline of mixed use developments. With two Silver Line Metro stations, Tysons draws workers, shoppers, and residents from across the region.", "benefits": ["Compete for visibility in one of the Mid Atlantic's busiest commercial districts", "Produce content that targets the massive daily flow of professionals and shoppers in Tysons", "Collect reviews from the high volume of customers passing through the Tysons area", "Run social media campaigns that tap into Tysons' energy as Northern Virginia's emerging downtown"]},
        "Burke": {"state": "VA", "desc": "a family friendly community in southern Fairfax County, Burke is centered around Burke Centre and Burke Lake Park. Known for strong neighborhood connections and excellent schools, businesses here thrive by building trust with the local families who make Burke their long term home.", "benefits": ["Get found by Burke families searching for trusted local services near Burke Centre", "Create family oriented content that resonates with Burke's stable residential community", "Build a strong review reputation among Burke Centre and Burke Lake area residents", "Engage Burke families on social media with content centered on community and trust"]},
        "Springfield": {"state": "VA", "desc": "a major transportation hub where I-95, I-395, and the Fairfax County Parkway converge, Springfield is home to the Springfield Town Center and Fort Belvoir's economic influence. Businesses here benefit from heavy traffic flow and a large, diverse customer base.", "benefits": ["Rank for high volume searches in the Springfield and Fort Belvoir area", "Develop content optimized for Springfield's busy commuter and military connected community", "Generate reviews from the diverse customer base around Springfield Town Center", "Maintain social media presence that reaches Springfield's large and active population"]},
        "Annandale": {"state": "VA", "desc": "known for its vibrant Korean food scene along Little River Turnpike and Columbia Pike, Annandale is one of the most culturally diverse communities in Fairfax County. Businesses here serve a multilingual customer base and compete in a dynamic, evolving market.", "benefits": ["Stand out in local search results across Annandale's diverse commercial corridors", "Create content that connects with Annandale's multicultural business community", "Build reviews that reflect your strong relationships with Annandale area customers", "Use social media to reach the culturally rich and engaged Annandale community"]},
        "Centreville": {"state": "VA", "desc": "a growing suburban center in western Fairfax County, Centreville is anchored by the Centreville Historic District and surrounded by family friendly neighborhoods like Centre Ridge and Sully Station. With easy access to I-66 and Route 29, businesses here serve a large and growing population.", "benefits": ["Capture local search traffic from Centreville and the Route 29 corridor", "Produce content that speaks to Centreville's family oriented suburban community", "Earn more online reviews from your customers in the Centreville and Sully area", "Build social media engagement with Centreville's growing network of families and professionals"]},
        "Chantilly": {"state": "VA", "desc": "home to the Smithsonian's National Air and Space Museum Udvar-Hazy Center and a thriving business corridor along Route 50, Chantilly is a commercial powerhouse in western Fairfax County. With data centers, office parks, and residential growth, the area offers businesses a large and diverse customer base.", "benefits": ["Rank for competitive searches in the Chantilly and Route 50 business corridor", "Create industry specific content that targets Chantilly's mix of residential and commercial customers", "Automate review requests from your Chantilly area clients and customers", "Grow your brand on social media across Chantilly's tech forward community"]},
        "Great Falls": {"state": "VA", "desc": "an affluent, semi rural community known for Great Falls Park along the Potomac River and its estate homes on spacious lots, Great Falls offers a countryside feel minutes from the capital. Businesses serving Great Falls cater to discerning homeowners who expect premium quality and personal attention.", "benefits": ["Appear in premium local searches from Great Falls' affluent homeowners", "Develop high quality content that matches the expectations of Great Falls residents", "Build a standout review profile that earns trust in this exclusive community", "Craft social media content that resonates with Great Falls' refined, nature loving audience"]},
        "Falls Church": {"state": "VA", "desc": "a small, independent city within the Fairfax County area, Falls Church is known for its top rated schools, walkable downtown along Broad Street, and the shops at West Falls. With proximity to both Arlington and Tysons, businesses in Falls Church enjoy strong local loyalty and regional visibility.", "benefits": ["Win local searches from Falls Church residents along Broad Street and West Falls", "Write content that highlights your presence in this tight knit, highly educated community", "Collect reviews that reinforce your reputation in the Falls Church area", "Engage the Falls Church community on social media with local, authentic content"]},
        "Oakton": {"state": "VA", "desc": "a quiet residential community at the crossroads of Route 123 and Hunter Mill Road, Oakton is home to families who value excellent schools and a suburban lifestyle close to Tysons and Vienna. Businesses here build success through word of mouth and strong local relationships.", "benefits": ["Show up when Oakton families search for trusted service providers nearby", "Create helpful content that positions your business as a go to resource in Oakton", "Turn happy Oakton customers into five star reviews with automated follow ups", "Stay visible to the Oakton community through consistent social media engagement"]},
        "Lorton": {"state": "VA", "desc": "located along I-95 in southern Fairfax County, Lorton has transformed from its industrial past into a vibrant community anchored by the Workhouse Arts Center and Laurel Hill. With the VRE station providing commuter access and new developments rising, businesses in Lorton have a growing audience.", "benefits": ["Capture search traffic from Lorton's growing residential and commuter community", "Publish content that highlights your connection to the revitalized Lorton area", "Build your review profile as Lorton continues to attract new residents and businesses", "Use social media to establish your brand in Lorton's evolving community landscape"]},
        "Clifton": {"state": "VA", "desc": "a picturesque historic town in southwestern Fairfax County, Clifton is known for its charming downtown, annual events like the Clifton Day festival, and its rural character within a suburban county. Businesses connected to Clifton benefit from fierce local loyalty and a community that supports its own.", "benefits": ["Get discovered by Clifton area residents who prefer supporting local businesses", "Create content that celebrates your connection to Clifton's historic and close knit community", "Earn authentic reviews from Clifton's loyal and engaged customer base", "Share community focused social media content that resonates with Clifton residents"]},
        "Mount Vernon": {"state": "VA", "desc": "the southeastern corner of Fairfax County along the Potomac River, Mount Vernon is best known for George Washington's historic estate but also includes vibrant communities along Route 1. With ongoing revitalization efforts and proximity to Fort Belvoir, businesses here serve a diverse and growing market.", "benefits": ["Rank for local searches along the Route 1 corridor and Mount Vernon district", "Develop content that connects your business to Mount Vernon's historic and evolving identity", "Generate reviews from the diverse customer base in the Mount Vernon area", "Build social media presence reaching Mount Vernon's mix of residents, tourists, and military families"]},
        "Alexandria (Fairfax)": {"state": "VA", "slug": "alexandria-fairfax-va", "desc": "the portions of Alexandria within Fairfax County, including areas like Kingstowne, Franconia, and the Van Dorn corridor, blend suburban convenience with proximity to Old Town Alexandria and DC. Businesses here tap into a large population base with strong spending power and diverse tastes.", "benefits": ["Capture searches from the Kingstowne, Franconia, and Van Dorn communities", "Create location specific content targeting Fairfax County's Alexandria neighborhoods", "Build reviews that establish your reputation across these growing suburban communities", "Run social media campaigns reaching the diverse professionals in Fairfax County's Alexandria area"]},
    },
    "Prince William County, VA": {
        "Manassas": {"state": "VA", "desc": "the independent City of Manassas and surrounding areas carry deep Civil War history alongside a revitalized Old Town with shops, restaurants, and a growing arts scene. Located at the junction of I-66 and Route 234, Manassas is a key commercial center for Prince William County businesses.", "benefits": ["Dominate local search results across Manassas and the Route 234 corridor", "Create content that highlights your roots in this historic and growing community", "Build a strong review presence that attracts customers from Old Town to the outer neighborhoods", "Engage the Manassas community on social media with content that reflects local pride"]},
        "Woodbridge": {"state": "VA", "desc": "one of the largest communities in Prince William County, Woodbridge stretches along I-95 and includes major retail centers like Potomac Mills and Stonebridge at Potomac Town Center. With a large and diverse population, businesses here need strong digital presence to stand out.", "benefits": ["Rank higher for competitive searches near Potomac Mills and Stonebridge", "Produce content that reaches Woodbridge's large and diverse consumer market", "Automate review collection from your high volume of Woodbridge area customers", "Build brand recognition on social media across one of Northern Virginia's most populated areas"]},
        "Gainesville": {"state": "VA", "desc": "one of the fastest growing communities in the region, Gainesville is centered around the Virginia Gateway shopping district and new residential developments along I-66. Young families flock here for affordable homes and modern amenities, creating strong demand for local services.", "benefits": ["Get found by the thousands of new families moving to the Gainesville area each year", "Create fresh content that addresses the needs of Gainesville's rapidly growing community", "Build your review profile as Gainesville's go to service provider near Virginia Gateway", "Reach new Gainesville residents through social media before your competitors do"]},
        "Haymarket": {"state": "VA", "desc": "a historic town at the western edge of Prince William County, Haymarket has grown from a quiet crossroads into a thriving community with neighborhoods like Dominion Valley and Piedmont. Businesses here serve an increasingly suburban population while maintaining connections to the area's rural heritage.", "benefits": ["Appear in local searches from Haymarket and the Dominion Valley community", "Write content that bridges Haymarket's historic charm and modern suburban growth", "Collect reviews from residents in Haymarket's expanding network of neighborhoods", "Use social media to connect with Haymarket families who value local, trusted businesses"]},
        "Dumfries": {"state": "VA", "desc": "one of the oldest towns in Virginia, Dumfries sits along Route 1 near Quantico Marine Corps Base. With a mix of military families and long time residents, plus proximity to major shopping at Potomac Mills, businesses here have a steady and loyal customer base.", "benefits": ["Rank for searches from Dumfries residents and the Quantico area military community", "Develop content that speaks to the unique needs of the Dumfries and Quantico corridor", "Generate reviews from Dumfries' loyal customer base of military and civilian families", "Build social media presence that connects with the Dumfries and Triangle communities"]},
        "Lake Ridge": {"state": "VA", "desc": "a well established residential community in eastern Prince William County, Lake Ridge is centered around its namesake lake and the Occoquan Reservoir. With tree lined neighborhoods and a strong sense of community, businesses serving Lake Ridge build success through trust and local reputation.", "benefits": ["Get discovered by Lake Ridge families searching for reliable local services", "Create community focused content that resonates with Lake Ridge homeowners", "Turn satisfied Lake Ridge customers into five star reviews automatically", "Engage the Lake Ridge community on social media with neighborhood relevant content"]},
        "Dale City": {"state": "VA", "desc": "one of the largest census designated places in Virginia, Dale City is a densely populated community along Dale Boulevard with its own commercial centers and a diverse population. Businesses here operate in a high demand market where digital visibility directly drives customer volume.", "benefits": ["Stand out in Dale City's competitive local search landscape with optimized SEO", "Produce targeted content that reaches Dale City's large and diverse population", "Scale your review collection across Dale City's high traffic commercial areas", "Run social media campaigns that penetrate Dale City's active online community"]},
        "Bristow": {"state": "VA", "desc": "a growing residential area between Manassas and Gainesville, Bristow is known for Jiffy Lube Live (the outdoor concert venue) and family friendly neighborhoods like Braemar and Kingsbrooke. The area continues to attract new residents drawn by its balance of suburban amenities and open space.", "benefits": ["Capture searches from Bristow residents in the Braemar and Kingsbrooke communities", "Write content that positions your business as a trusted resource in the growing Bristow area", "Build reviews that establish your reputation among Bristow's family oriented households", "Connect with new Bristow residents on social media before they find your competitors"]},
        "Nokesville": {"state": "VA", "desc": "a rural community in southern Prince William County, Nokesville maintains a country feel with horse farms, open fields, and a tight knit community around Nokesville Road. Businesses here earn loyalty through personal service and genuine community connections.", "benefits": ["Be the first result when Nokesville area residents search for local services", "Create authentic content that reflects your understanding of the Nokesville community", "Earn genuine reviews from Nokesville's loyal and word of mouth driven customer base", "Use social media to maintain visibility in Nokesville's close knit rural community"]},
        "Occoquan": {"state": "VA", "desc": "a small, historic waterfront town along the Occoquan River, Occoquan is known for its art galleries, antique shops, and seasonal craft shows that draw visitors from across the region. Businesses here serve both local residents and a steady stream of tourists exploring the town's charming Mill Street.", "benefits": ["Attract visitors and locals searching for services near the Occoquan waterfront", "Create content that highlights your business's connection to Occoquan's artisan community", "Build a review profile that appeals to the discerning visitors exploring Mill Street", "Share visually rich social media content showcasing your Occoquan area presence"]},
        "Triangle": {"state": "VA", "desc": "located adjacent to Quantico Marine Corps Base along I-95, Triangle serves as a gateway community for military personnel and their families. With the National Museum of the Marine Corps nearby, the area combines patriotic heritage with the practical needs of a military connected population.", "benefits": ["Rank for local searches from military families and residents near Quantico", "Develop content that speaks to the Triangle and Quantico community's unique needs", "Collect reviews from the steady base of military and civilian customers in Triangle", "Maintain social media presence that welcomes incoming military families to the Triangle area"]},
        "Montclair": {"state": "VA", "desc": "a well planned residential community in eastern Prince William County, Montclair features its own lake, golf course, and recreation facilities. Bordered by the Occoquan Reservoir and Prince William Forest Park, Montclair residents enjoy a nature surrounded suburban lifestyle.", "benefits": ["Show up in searches from Montclair residents looking for convenient local services", "Create content that connects with Montclair's active, nature oriented community", "Generate reviews from your Montclair area customers with automated follow up systems", "Build social media engagement with the Montclair community's outdoor lifestyle focus"]},
        "Potomac Shores": {"state": "VA", "desc": "a newer master planned community along the Potomac River, Potomac Shores features a Jack Nicklaus designed golf course, a VRE station, and modern amenities. As one of Prince William County's newest developments, businesses here have the opportunity to establish themselves early with a growing population.", "benefits": ["Position your business as the go to provider for Potomac Shores' new residents", "Create content that welcomes newcomers and establishes your brand in this growing community", "Be the first to build a strong review profile in this emerging market", "Launch social media campaigns targeting the young professionals moving to Potomac Shores"]},
    },
    "Montgomery County, MD": {
        "Rockville": {"state": "MD", "desc": "the county seat of Montgomery County, Rockville features a revitalized Town Center, the Rockville Metro station, and a diverse business community along Rockville Pike. From biotech firms to local restaurants, Rockville's competitive market demands strong digital marketing to stand out.", "benefits": ["Rank higher along the Rockville Pike corridor and near Rockville Town Center", "Create content that targets Rockville's mix of commuters, professionals, and families", "Build a standout review profile in one of Maryland's most competitive business markets", "Grow your social media reach across Rockville's diverse and digitally connected community"]},
        "Bethesda": {"state": "MD", "desc": "an upscale community just northwest of Washington, DC, Bethesda is home to the National Institutes of Health, Walter Reed Medical Center, and a vibrant downtown filled with restaurants, boutiques, and galleries along Bethesda Row. Businesses here cater to one of the most affluent and educated populations in the country.", "benefits": ["Compete for premium searches in Bethesda's high value, affluent market", "Develop sophisticated content that matches Bethesda's professional and cultured audience", "Build an exceptional review profile that earns trust near Bethesda Row and NIH", "Create polished social media content for Bethesda's discerning consumer base"]},
        "Silver Spring": {"state": "MD", "desc": "a vibrant, diverse urban center just across the DC border, Silver Spring has transformed its downtown with the Silver Spring Civic Building, AFI Silver Theatre, and a bustling dining scene along Georgia Avenue and Colesville Road. Businesses here serve one of the most culturally diverse communities in Maryland.", "benefits": ["Stand out in Silver Spring's diverse and competitive local search results", "Produce multicultural content that connects with Silver Spring's vibrant community", "Generate reviews from the high volume of customers in downtown Silver Spring", "Build social media engagement across Silver Spring's culturally rich and active audience"]},
        "Germantown": {"state": "MD", "desc": "one of the largest communities in Montgomery County, Germantown stretches along the I-270 corridor with shopping centers, parks, and a diverse residential population. With continued growth and development near the Germantown Town Center, businesses here need digital strategies to reach this large suburban market.", "benefits": ["Capture search traffic from Germantown's large and growing I-270 corridor community", "Create content that resonates with Germantown's family oriented, diverse population", "Scale your review collection across Germantown's sprawling residential neighborhoods", "Build brand awareness on social media across one of Montgomery County's most populated areas"]},
        "Gaithersburg": {"state": "MD", "desc": "a city known for its blend of urban and suburban character, Gaithersburg features the Kentlands mixed use development, the Rio Washingtonian Center, and the NIST campus. With strong biotech and tech sectors along the I-270 corridor, businesses here serve a highly educated and diverse market.", "benefits": ["Rank for competitive searches near Kentlands, Rio, and the I-270 tech corridor", "Develop technical and lifestyle content for Gaithersburg's professional community", "Build reviews that set you apart in Gaithersburg's innovation driven marketplace", "Engage Gaithersburg's diverse professionals and families through targeted social media"]},
        "Potomac": {"state": "MD", "desc": "one of the wealthiest communities in the Washington, DC area, Potomac is known for its expansive estates, top rated schools, and proximity to Great Falls along the Potomac River. Businesses serving Potomac cater to clients who expect premium quality and personalized attention.", "benefits": ["Position your business for high value searches in the Potomac area", "Create premium content that reflects the quality Potomac residents expect", "Build a five star review profile worthy of one of Maryland's most exclusive communities", "Develop a refined social media presence that connects with Potomac's affluent families"]},
        "Olney": {"state": "MD", "desc": "a family oriented community in northeastern Montgomery County, Olney is centered around the Olney Town Center and maintains a suburban charm with easy access to major routes. Known for the annual Olney Days festival and strong community involvement, businesses here build success through local trust.", "benefits": ["Get found by Olney families searching for reliable, community minded businesses", "Write content that connects with Olney's strong sense of local community", "Collect reviews that reinforce your reputation in the Olney Town Center area", "Engage Olney residents on social media with family and community focused content"]},
        "Wheaton": {"state": "MD", "desc": "a culturally diverse community anchored by the Wheaton Metro station and the vibrant Wheaton Triangle commercial district, Wheaton has undergone significant revitalization. With Brookside Gardens nearby and a thriving international food scene, businesses here serve a dynamic and growing market.", "benefits": ["Stand out in local search results across the Wheaton Triangle and Metro area", "Create diverse content that reflects Wheaton's multicultural business community", "Build reviews that highlight your connection to Wheaton's revitalizing commercial district", "Use social media to reach Wheaton's culturally diverse and engaged population"]},
        "Takoma Park": {"state": "MD", "desc": "known as Azalea City and celebrated for its progressive community spirit, Takoma Park features a walkable downtown, the historic Takoma Theatre, and a beloved farmers market. Businesses here thrive by connecting with residents who value local, independent, and community oriented services.", "benefits": ["Connect with Takoma Park's loyal, shop local customer base through SEO", "Create authentic content that aligns with Takoma Park's community first values", "Earn reviews from Takoma Park residents who actively support local businesses", "Build social media presence that reflects Takoma Park's independent, creative spirit"]},
        "Chevy Chase": {"state": "MD", "desc": "an affluent community bordering Washington, DC, Chevy Chase is known for the upscale shops along Wisconsin Avenue, the Chevy Chase Pavilion, and beautiful residential neighborhoods. Businesses here serve a sophisticated clientele with high expectations for quality and service.", "benefits": ["Compete for premium searches in the affluent Chevy Chase and Wisconsin Avenue area", "Develop polished content that meets the high standards of Chevy Chase residents", "Build an elite review profile that matches the quality expectations of this community", "Create refined social media content for Chevy Chase's sophisticated audience"]},
        "Kensington": {"state": "VA", "slug": "kensington-md", "state_full": "Maryland", "desc": "a historic town in central Montgomery County, Kensington charms with its Antique Row along Howard Avenue and a walkable downtown with local shops and restaurants. Businesses here benefit from a loyal community that values character, history, and personal service.", "benefits": ["Get discovered by Kensington residents exploring local businesses along Antique Row", "Create content that celebrates Kensington's historic charm and small town appeal", "Build reviews from Kensington's loyal, community minded customer base", "Share Kensington's unique character through engaging social media content"]},
        "Poolesville": {"state": "MD", "desc": "a small agricultural town in western Montgomery County, Poolesville is known for its rural character, the nearby Sugarloaf Mountain, and a strong sense of community. Businesses here serve a loyal local customer base and the visitors drawn to the surrounding farmland and natural beauty.", "benefits": ["Be the top search result for services in Poolesville and western Montgomery County", "Write content that reflects your connection to Poolesville's rural, close knit community", "Earn authentic reviews from Poolesville's loyal and supportive customer base", "Use social media to reach both residents and visitors near Sugarloaf Mountain"]},
        "Clarksburg": {"state": "MD", "desc": "one of Montgomery County's fastest growing communities, Clarksburg features new developments like Clarksburg Village and Clarksburg Town Center along I-270. With thousands of new homes and families arriving, businesses here have a unique opportunity to establish themselves in an emerging market.", "benefits": ["Position your business early in Clarksburg's fast growing new home community", "Create content that welcomes new Clarksburg residents and introduces your services", "Be the first to build a strong review profile in this emerging Montgomery County market", "Reach new Clarksburg families on social media before competitors establish their presence"]},
        "Damascus": {"state": "MD", "desc": "a quiet community in northern Montgomery County, Damascus maintains a small town atmosphere with local shops along Main Street and surrounding farmland. Known for the annual Damascus Community Fair, businesses here succeed through genuine community relationships.", "benefits": ["Rank first when Damascus residents search for trusted local services", "Develop content that highlights your local presence in the Damascus community", "Build reviews that reflect the trust Damascus residents place in neighborhood businesses", "Stay connected with the Damascus community through consistent social media engagement"]},
        "Burtonsville": {"state": "MD", "desc": "located at the crossroads of Route 29 and Route 198 in eastern Montgomery County, Burtonsville serves as a gateway between Montgomery and Howard counties. With a mix of established neighborhoods and commercial centers, businesses here draw customers from a wide surrounding area.", "benefits": ["Capture search traffic from the Route 29 and Route 198 corridor in Burtonsville", "Create content targeting the wide catchment area around Burtonsville's commercial centers", "Generate reviews from customers spanning the Burtonsville and eastern Montgomery County area", "Build social media visibility across the communities connected by Burtonsville's key intersections"]},
    },
    "Baltimore County, MD": {
        "Towson": {"state": "MD", "desc": "the county seat of Baltimore County, Towson is a thriving commercial center anchored by Towson Town Center, Towson University, and a growing downtown with restaurants and offices. Businesses here compete in a dynamic market fueled by college students, professionals, and suburban families.", "benefits": ["Rank higher in Towson's competitive market near Towson Town Center and the university", "Create content that reaches Towson's mix of students, professionals, and families", "Build a strong review profile in one of Baltimore County's busiest commercial districts", "Grow your social media following across Towson's energetic and engaged community"]},
        "Catonsville": {"state": "MD", "desc": "known as Music City Maryland, Catonsville features a charming Main Street, UMBC's campus, and a strong arts community. Located along Frederick Road west of Baltimore, businesses here serve a loyal customer base that values local character and community connections.", "benefits": ["Get found by Catonsville residents searching for services along Frederick Road and Main Street", "Create content that aligns with Catonsville's arts focused, community minded identity", "Earn reviews from Catonsville's loyal customer base who prefer supporting local businesses", "Build social media presence that celebrates Catonsville's Music City heritage"]},
        "Pikesville": {"state": "MD", "desc": "a well established community northwest of Baltimore along Reisterstown Road and Old Court Road, Pikesville is known for its diverse population, excellent delis, and strong business community. Businesses here serve a loyal and connected customer base.", "benefits": ["Stand out in local searches across the Pikesville and Old Court Road corridor", "Develop content that connects with Pikesville's diverse and established community", "Build a review profile that reflects your deep roots in the Pikesville area", "Engage Pikesville's connected community through consistent social media content"]},
        "Dundalk": {"state": "MD", "desc": "a proud working class community on the Patapsco River east of Baltimore, Dundalk has a strong industrial heritage and tight community bonds. With the revitalization of Dundalk's waterfront and commercial areas along Dundalk Avenue, businesses here have new opportunities to grow.", "benefits": ["Rank for local searches in Dundalk and the surrounding Patapsco waterfront area", "Create honest, straightforward content that resonates with Dundalk's hardworking community", "Generate reviews from Dundalk's loyal customers who value reliability and quality", "Use social media to connect with Dundalk's proud, community oriented residents"]},
        "Essex": {"state": "MD", "desc": "a community in eastern Baltimore County known for its waterfront access along Back River, Essex features a mix of residential neighborhoods and commercial centers along Eastern Boulevard. Businesses here serve a large suburban population with strong community ties.", "benefits": ["Capture local searches from Essex residents along Eastern Boulevard and Back River", "Write content that connects with Essex's large and established suburban community", "Build your review reputation across Essex's network of neighborhoods and shopping centers", "Grow your social media presence among Essex's community minded residents"]},
        "Perry Hall": {"state": "MD", "desc": "a family oriented community in northeastern Baltimore County, Perry Hall is centered around the Perry Hall Town Center and known for excellent schools and safe neighborhoods. Businesses here build success through the trust and loyalty of long term resident families.", "benefits": ["Get discovered by Perry Hall families looking for reliable neighborhood services", "Create family focused content that speaks to Perry Hall's suburban lifestyle", "Collect five star reviews from Perry Hall's loyal family customer base", "Engage Perry Hall families on social media with community relevant content"]},
        "Parkville": {"state": "MD", "desc": "a large residential community north of Baltimore, Parkville is centered around Loch Raven Boulevard and Perring Parkway with a mix of established neighborhoods and commercial corridors. Businesses here serve a stable, community oriented population.", "benefits": ["Rank for searches along the Loch Raven Boulevard and Perring Parkway corridors", "Develop content that reaches Parkville's large and stable residential community", "Build reviews from Parkville's loyal customer base in this established Baltimore suburb", "Maintain social media visibility across Parkville's interconnected neighborhood network"]},
        "Owings Mills": {"state": "MD", "desc": "a growing community in northwestern Baltimore County, Owings Mills features the Metro Centre at Owings Mills, the Foundry Row shopping center, and convenient Metro access. With ongoing development and a diverse population, businesses here compete in an evolving market.", "benefits": ["Stand out in Owings Mills' growing and competitive commercial market", "Create content targeting Owings Mills' diverse mix of professionals and families", "Build reviews that establish your credibility near Metro Centre and Foundry Row", "Grow your social media following in Owings Mills' expanding and diverse community"]},
        "Cockeysville": {"state": "MD", "desc": "located along York Road in the Hunt Valley corridor, Cockeysville combines residential neighborhoods with commercial development near the Hunt Valley Towne Centre. Businesses here benefit from the area's strong economic activity and family oriented communities.", "benefits": ["Capture searches from the Cockeysville and York Road corridor", "Write content that targets the families and professionals in the Cockeysville area", "Generate reviews from your Cockeysville customers near Hunt Valley Towne Centre", "Build social media presence across the Cockeysville and Loch Raven area communities"]},
        "Hunt Valley": {"state": "MD", "desc": "a major business and retail center in northern Baltimore County, Hunt Valley is home to the Hunt Valley Towne Centre, corporate offices, and the NCR Trail. The area attracts professionals and outdoor enthusiasts who value both career opportunities and quality of life.", "benefits": ["Rank for searches in the Hunt Valley business district and Towne Centre area", "Create professional content that connects with Hunt Valley's corporate and retail audience", "Build reviews from the high volume of professionals and shoppers in Hunt Valley", "Develop social media content that highlights your Hunt Valley area business presence"]},
        "Timonium": {"state": "MD", "desc": "known for the Maryland State Fairgrounds and its location along York Road between Towson and Hunt Valley, Timonium is a well connected community with strong commercial activity. Businesses here benefit from year round traffic and seasonal events that draw visitors from across the state.", "benefits": ["Get found by Timonium residents and fairgrounds visitors searching for local services", "Create content that leverages Timonium's central location along the York Road corridor", "Build reviews from both regular customers and seasonal visitors to the Timonium area", "Use social media to stay visible during peak fairgrounds events and throughout the year"]},
        "Reisterstown": {"state": "MD", "desc": "a historic community along Reisterstown Road in northwestern Baltimore County, Reisterstown features a traditional Main Street, family neighborhoods, and access to nearby Liberty Reservoir. Businesses here serve a stable community that values local connections.", "benefits": ["Rank for local searches along Reisterstown Road and the surrounding communities", "Write content that highlights your deep connection to the Reisterstown area", "Earn reviews from Reisterstown's loyal, community oriented customer base", "Stay connected with Reisterstown residents through regular social media engagement"]},
        "Randallstown": {"state": "MD", "desc": "a diverse community in western Baltimore County centered around Liberty Road, Randallstown is home to the Randallstown Community Center and a growing population of families and professionals. Businesses here serve a dynamic market with strong community involvement.", "benefits": ["Stand out in local searches across the Liberty Road and Randallstown corridor", "Create content that connects with Randallstown's diverse and growing community", "Generate reviews from Randallstown's active and community minded residents", "Build social media engagement across Randallstown's vibrant neighborhood network"]},
        "Middle River": {"state": "MD", "desc": "a waterfront community in eastern Baltimore County along the Middle River and Chesapeake Bay watershed, Middle River offers a mix of suburban living and waterfront recreation. With marinas, parks, and a large residential population, businesses here serve customers who enjoy an active outdoor lifestyle.", "benefits": ["Capture searches from Middle River's large waterfront and suburban community", "Create content that connects with Middle River's outdoor and waterfront lifestyle", "Build reviews from Middle River residents who value reliable local businesses", "Use social media to reach Middle River's active, recreation oriented community"]},
        "Lutherville": {"state": "MD", "desc": "a charming residential community just north of Towson, Lutherville (often paired with Timonium) features tree lined streets, local shops, and convenient access to the Light Rail. Businesses here serve an established, family oriented population that values quality and convenience.", "benefits": ["Get discovered by Lutherville families looking for trusted nearby services", "Write content that speaks to Lutherville's established, quality focused community", "Collect reviews from loyal Lutherville area customers with automated follow ups", "Engage Lutherville residents on social media with neighborhood focused content"]},
        "White Marsh": {"state": "MD", "desc": "a major retail and commercial hub in eastern Baltimore County, White Marsh is anchored by the Avenue at White Marsh shopping center and surrounded by growing residential developments. With heavy retail traffic and a large customer base, businesses here need strong digital presence to compete.", "benefits": ["Rank in the competitive White Marsh retail corridor near the Avenue at White Marsh", "Create content optimized for high volume commercial searches in the White Marsh area", "Build reviews that help you stand out among the many businesses near White Marsh", "Grow your social media presence to capture the large audience shopping in White Marsh"]},
        "Arbutus": {"state": "MD", "desc": "a close knit community in southwestern Baltimore County near UMBC, Arbutus maintains a small town feel with local shops and a strong community identity. Businesses here benefit from loyal neighborhood customers and the energy of the nearby university campus.", "benefits": ["Show up in searches from Arbutus residents and UMBC area customers", "Create local content that reflects Arbutus's neighborhood charm and community spirit", "Earn authentic reviews from Arbutus's loyal and supportive customer base", "Use social media to connect with both Arbutus residents and the nearby UMBC community"]},
    },
}

# Fix Kensington state
locations["Montgomery County, MD"]["Kensington"]["state"] = "MD"

def slug_for(city, data):
    if "slug" in data:
        return data["slug"]
    return city.lower().replace(" ", "-").replace("(", "").replace(")", "") + "-" + data["state"].lower()

def generate_page(city, data, county):
    state_full = {"VA": "Virginia", "MD": "Maryland"}[data["state"]]
    slug = slug_for(city, data)
    
    benefits_html = ""
    for b in data["benefits"]:
        benefits_html += f'      <div class="pain-card reveal">\n        <h3>{b.split(" ", 4)[-1][:50].rsplit(" ", 1)[0] if len(b) > 50 else b}</h3>\n        <p>{b}</p>\n      </div>\n'

    # Actually let's make proper benefit cards with icons
    icons = ["📈", "📝", "⭐", "📱"]
    titles = ["Local SEO Dominance", "Content That Converts", "Review Generation", "Social Media Growth"]
    benefits_html = ""
    for i, b in enumerate(data["benefits"]):
        benefits_html += f'      <div class="pain-card reveal">\n        <div class="pain-icon">{icons[i]}</div>\n        <h3>{titles[i]}</h3>\n        <p>{b}</p>\n      </div>\n'

    display_city = city.replace(" (Fairfax)", " (Fairfax County)")
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Employees for Businesses in {display_city}, {state_full} | Get Next Level Marketing</title>
<meta name="description" content="Custom AI employees for businesses in {display_city}, {state_full}. Automate your SEO, content creation, review management, and social media. Starting at $500/month.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg-primary:#ffffff;
  --bg-secondary:#f8fafc;
  --bg-card:#ffffff;
  --bg-card-hover:#f1f5f9;
  --accent-blue:#2563eb;
  --accent-blue-glow:#2563eb20;
  --accent-orange:#ea580c;
  --accent-orange-glow:#ea580c20;
  --text-primary:#0f172a;
  --text-secondary:#475569;
  --text-muted:#94a3b8;
  --border:#e2e8f0;
  --border-light:#cbd5e1;
  --gradient-blue:linear-gradient(135deg,#3b82f6,#2563eb);
  --gradient-orange:linear-gradient(135deg,#f97316,#ea580c);
}}
html{{scroll-behavior:smooth;scroll-padding-top:80px}}
body{{font-family:'Inter',system-ui,sans-serif;background:var(--bg-primary);color:var(--text-primary);line-height:1.7;overflow-x:hidden;font-size:17px}}
a{{color:var(--accent-blue);text-decoration:none;transition:color .2s}}
a:hover{{color:#60a5fa}}
img{{max-width:100%;display:block}}
.container{{max-width:1140px;margin:0 auto;padding:0 24px}}
.section{{padding:100px 0}}
.section-label{{font-size:.8rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--accent-blue);margin-bottom:12px}}
.section-title{{font-size:clamp(2rem,4vw,2.75rem);font-weight:800;line-height:1.15;margin-bottom:20px}}
.section-subtitle{{font-size:1.15rem;color:var(--text-secondary);max-width:640px;line-height:1.7}}
.text-center{{text-align:center}}
.mx-auto{{margin-left:auto;margin-right:auto}}
.reveal{{opacity:0;transform:translateY(30px);transition:opacity .7s ease,transform .7s ease}}
.reveal.visible{{opacity:1;transform:translateY(0)}}
.header{{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(255,255,255,.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);transition:all .3s}}
.header-inner{{display:flex;align-items:center;justify-content:space-between;height:72px}}
.logo{{font-size:1.25rem;font-weight:800;color:var(--text-primary)}}
.logo span{{color:var(--accent-orange)}}
.nav{{display:flex;align-items:center;gap:32px}}
.nav a{{color:var(--text-secondary);font-size:.9rem;font-weight:500;transition:color .2s}}
.nav a:hover{{color:var(--text-primary)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;padding:12px 28px;border-radius:8px;font-weight:600;font-size:.95rem;transition:all .25s;cursor:pointer;border:none;text-decoration:none}}
.btn-primary{{background:var(--gradient-blue);color:#fff;box-shadow:0 4px 20px var(--accent-blue-glow)}}
.btn-primary:hover{{transform:translateY(-2px);box-shadow:0 8px 30px var(--accent-blue-glow);color:#fff}}
.btn-orange{{background:var(--gradient-orange);color:#fff;box-shadow:0 4px 20px var(--accent-orange-glow)}}
.btn-orange:hover{{transform:translateY(-2px);box-shadow:0 8px 30px var(--accent-orange-glow);color:#fff}}
.btn-outline{{border:1px solid var(--border-light);color:var(--text-primary);background:transparent}}
.btn-outline:hover{{border-color:var(--accent-blue);color:var(--accent-blue)}}
.btn-sm{{padding:8px 20px;font-size:.85rem}}
.mobile-toggle{{display:none;background:none;border:none;color:var(--text-primary);font-size:1.5rem;cursor:pointer}}
@media(max-width:768px){{
  .nav{{display:none;position:absolute;top:72px;left:0;right:0;background:#ffffff;flex-direction:column;padding:24px;gap:20px;border-bottom:1px solid var(--border)}}
  .nav.open{{display:flex}}
  .mobile-toggle{{display:block}}
}}
.hero{{padding:160px 0 100px;position:relative;overflow:hidden}}
.hero::before{{content:'';position:absolute;top:-200px;right:-200px;width:600px;height:600px;background:radial-gradient(circle,#3b82f610 0%,transparent 70%);pointer-events:none}}
.hero::after{{content:'';position:absolute;bottom:-100px;left:-200px;width:500px;height:500px;background:radial-gradient(circle,#f9731610 0%,transparent 70%);pointer-events:none}}
.hero h1{{font-size:clamp(2.5rem,5.5vw,3.5rem);font-weight:900;line-height:1.08;margin-bottom:24px;max-width:780px}}
.hero h1 .highlight{{background:var(--gradient-orange);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.hero p{{font-size:1.2rem;color:var(--text-secondary);max-width:600px;margin-bottom:36px;line-height:1.7}}
.hero-ctas{{display:flex;gap:16px;flex-wrap:wrap}}
.hero-trust{{margin-top:48px;display:flex;align-items:center;gap:12px;color:var(--text-muted);font-size:.85rem}}
.hero-trust .shield{{font-size:1.2rem}}
.pain-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:48px}}
.pain-card{{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:32px;transition:all .3s;box-shadow:0 1px 3px rgba(0,0,0,.06)}}
.pain-card:hover{{border-color:var(--accent-blue);transform:translateY(-4px)}}
.pain-icon{{font-size:2rem;margin-bottom:16px}}
.pain-card h3{{font-size:1.15rem;font-weight:700;margin-bottom:8px}}
.pain-card p{{color:var(--text-secondary);font-size:1rem}}
.skills-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin-top:48px}}
.skill-item{{display:flex;align-items:center;gap:14px;padding:20px 24px;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;transition:all .3s}}
.skill-item:hover{{border-color:var(--accent-orange);background:var(--bg-card-hover)}}
.skill-icon{{font-size:1.4rem;flex-shrink:0}}
.skill-item h4{{font-size:.95rem;font-weight:600}}
.skill-item p{{font-size:.8rem;color:var(--text-muted);margin-top:2px}}
.pricing-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:32px;margin-top:48px;max-width:820px;margin-left:auto;margin-right:auto;align-items:start}}
.pricing-card{{background:var(--bg-card);border:1px solid var(--border);border-radius:20px;padding:40px;position:relative;transition:all .3s;box-shadow:0 1px 3px rgba(0,0,0,.06);display:flex;flex-direction:column}}
.pricing-card:hover{{transform:translateY(-4px)}}
.pricing-card.featured{{border-color:var(--accent-orange);box-shadow:0 8px 30px var(--accent-orange-glow)}}
.pricing-badge{{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--gradient-orange);color:#fff;padding:6px 20px;border-radius:100px;font-size:.8rem;font-weight:700;white-space:nowrap}}
.pricing-card h3{{font-size:1.2rem;font-weight:700;margin-bottom:4px}}
.pricing-card .desc{{color:var(--text-muted);font-size:.9rem;margin-bottom:20px}}
.price{{font-size:3rem;font-weight:900;line-height:1}}
.price span{{font-size:1rem;font-weight:500;color:var(--text-muted)}}
.price-note{{font-size:.85rem;color:var(--text-muted);margin-top:4px;margin-bottom:28px}}
.pricing-features{{list-style:none;margin-bottom:32px;flex-grow:1}}
.pricing-features li{{padding:12px 0;border-bottom:1px solid var(--border);font-size:1rem;color:var(--text-secondary);display:flex;align-items:flex-start;gap:10px}}
.pricing-features li:last-child{{border:none}}
.pricing-features .check{{color:#22c55e;font-weight:700;flex-shrink:0}}
.pricing-card .btn{{width:100%}}
.cta-section{{background:linear-gradient(135deg,#eff6ff 0%,#f0f9ff 100%);position:relative;overflow:hidden}}
.cta-section::before{{content:'';position:absolute;top:-100px;right:-100px;width:400px;height:400px;background:radial-gradient(circle,#3b82f610,transparent 70%);pointer-events:none}}
.cta-box{{text-align:center;max-width:640px;margin:0 auto;position:relative;z-index:1}}
.cta-box h2{{font-size:clamp(1.8rem,3.5vw,2.5rem);font-weight:800;margin-bottom:16px}}
.cta-box p{{color:var(--text-secondary);font-size:1.05rem;margin-bottom:32px}}
.footer{{padding:40px 0;border-top:1px solid var(--border);text-align:center;color:var(--text-muted);font-size:.85rem}}
.footer a{{color:var(--text-secondary)}}
</style>
</head>
<body>

<header class="header">
  <div class="container header-inner">
    <a href="/" class="logo">Next Level <span>AI</span></a>
    <button class="mobile-toggle" onclick="document.querySelector('.nav').classList.toggle('open')" aria-label="Menu">&#9776;</button>
    <nav class="nav">
      <a href="/#how-it-works">How It Works</a>
      <a href="/#skills">Skills</a>
      <a href="/#pricing">Pricing</a>
      <a href="/#faq">FAQ</a>
      <a href="https://capital-cyber.com/rick" class="btn btn-primary btn-sm">Book a Call</a>
    </nav>
  </div>
</header>

<section class="hero">
  <div class="container">
    <h1>AI Employees for Businesses in <span class="highlight">{display_city}, {state_full}</span></h1>
    <p>Serving {county}, {data["desc"]}</p>
    <div class="hero-ctas">
      <a href="https://capital-cyber.com/rick" class="btn btn-orange">Book Your Free Strategy Call</a>
      <a href="#pricing" class="btn btn-outline">See Pricing</a>
    </div>
    <div class="hero-trust">
      <span class="shield">&#128274;</span> Built and secured by Capital Cyber cybersecurity engineers
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="text-center">
      <div class="section-label">Why AI Employees</div>
      <h2 class="section-title">Grow Your {display_city} Business With AI Powered Marketing</h2>
      <p class="section-subtitle mx-auto">Stop losing customers to competitors with better online presence. Your AI employee handles the marketing so you can focus on what you do best.</p>
    </div>
    <div class="pain-grid">
{benefits_html}    </div>
  </div>
</section>

<section class="section" id="skills" style="background:var(--bg-secondary)">
  <div class="container">
    <div class="text-center">
      <div class="section-label">What Your AI Employee Can Do</div>
      <h2 class="section-title">Marketing Skills Built for {display_city} Businesses</h2>
      <p class="section-subtitle mx-auto">From SEO and content creation to review management and social media. Start with 5 skills or go unlimited.</p>
    </div>
    <div class="skills-grid">
      <div class="skill-item reveal">
        <span class="skill-icon">&#128205;</span>
        <div><h4>Location Page Builder</h4><p>SEO optimized pages for every city and service area you cover.</p></div>
      </div>
      <div class="skill-item reveal">
        <span class="skill-icon">&#128221;</span>
        <div><h4>Blog and Content Creation</h4><p>Consistent, keyword rich blog posts that drive organic traffic.</p></div>
      </div>
      <div class="skill-item reveal">
        <span class="skill-icon">&#128269;</span>
        <div><h4>SEO Optimization</h4><p>On page SEO, meta tags, schema markup, and keyword strategy.</p></div>
      </div>
      <div class="skill-item reveal">
        <span class="skill-icon">&#11088;</span>
        <div><h4>Review Request Follow Ups</h4><p>Automatic review requests after every completed job.</p></div>
      </div>
      <div class="skill-item reveal">
        <span class="skill-icon">&#128172;</span>
        <div><h4>Website Live Chat</h4><p>Instant answers on your website, day or night.</p></div>
      </div>
      <div class="skill-item reveal">
        <span class="skill-icon">&#128231;</span>
        <div><h4>Email Marketing</h4><p>Newsletters, promotions, and drip campaigns that keep customers coming back.</p></div>
      </div>
      <div class="skill-item reveal">
        <span class="skill-icon">&#128202;</span>
        <div><h4>Daily Business Reports</h4><p>Morning briefings on performance, tasks, and what needs attention.</p></div>
      </div>
      <div class="skill-item reveal">
        <span class="skill-icon">&#128241;</span>
        <div><h4>Social Media Management</h4><p>Consistent posts across platforms. Show up where your customers scroll.</p></div>
      </div>
      <div class="skill-item reveal">
        <span class="skill-icon">&#129534;</span>
        <div><h4>Estimate Follow Ups</h4><p>Automatic follow ups on pending estimates to close more jobs.</p></div>
      </div>
      <div class="skill-item reveal">
        <span class="skill-icon">&#127959;</span>
        <div><h4>Service Page Builder</h4><p>Dedicated pages for each service you offer, optimized to rank and convert.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="pricing">
  <div class="container text-center">
    <div class="section-label">Simple Pricing</div>
    <h2 class="section-title">Two Plans. No Hidden Fees. Cancel Anytime.</h2>
    <p class="section-subtitle mx-auto">Everything you need to deploy a secure AI employee for your {display_city} business.</p>
    <div class="pricing-grid">
      <div class="pricing-card reveal">
        <h3>AI Employee</h3>
        <p class="desc">Perfect for getting started</p>
        <div class="price">$500<span>/month</span></div>
        <p class="price-note">LLM usage included</p>
        <ul class="pricing-features">
          <li><span class="check">&#10003;</span> Custom AI employee built for your business</li>
          <li><span class="check">&#10003;</span> Up to 5 skills</li>
          <li><span class="check">&#10003;</span> Single platform deployment</li>
          <li><span class="check">&#10003;</span> Full security hardening</li>
          <li><span class="check">&#10003;</span> LLM usage included</li>
          <li><span class="check">&#10003;</span> Monthly optimization check in</li>
          <li><span class="check">&#10003;</span> Ongoing management and support</li>
        </ul>
        <a href="https://capital-cyber.com/rick" class="btn btn-primary">Get Started</a>
      </div>
      <div class="pricing-card featured reveal">
        <div class="pricing-badge">Most Popular</div>
        <h3>AI Employee Pro</h3>
        <p class="desc">For businesses ready to go all in</p>
        <div class="price">$1,000<span>/month</span></div>
        <p class="price-note">Full LLM usage included</p>
        <ul class="pricing-features">
          <li><span class="check">&#10003;</span> Custom AI employee built for your business</li>
          <li><span class="check">&#10003;</span> Unlimited skills</li>
          <li><span class="check">&#10003;</span> Multi platform deployment (web, SMS, email)</li>
          <li><span class="check">&#10003;</span> Full security hardening</li>
          <li><span class="check">&#10003;</span> Full LLM usage included (premium models)</li>
          <li><span class="check">&#10003;</span> Weekly optimization and reporting</li>
          <li><span class="check">&#10003;</span> Priority support</li>
          <li><span class="check">&#10003;</span> Custom knowledge base</li>
          <li><span class="check">&#10003;</span> Advanced integrations (CRM, booking, inventory)</li>
        </ul>
        <a href="https://capital-cyber.com/rick" class="btn btn-orange">Get Started</a>
      </div>
    </div>
  </div>
</section>

<section class="section cta-section">
  <div class="container">
    <div class="cta-box">
      <h2>Ready to Add an AI Employee to Your {display_city} Team?</h2>
      <p>Book a free strategy call. We will talk about your business, identify the right AI employee, and show you exactly how we would build and secure it for your {display_city} location. No pressure. No obligation.</p>
      <a href="https://capital-cyber.com/rick" class="btn btn-orange" style="font-size:1.1rem;padding:16px 40px">Book Your Free Strategy Call</a>
      <p style="margin-top:16px;font-size:.85rem;color:var(--text-muted)">30 minute call with Rick, our COO</p>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <p>&copy; 2026 Get Next Level Marketing. AI employees powered by <a href="http://capital-cyber.com/?utm_source=direct&utm_medium=direct&utm_campaign=getnextlevelmarketing">Capital Cyber</a> cybersecurity engineers.</p>
  </div>
</footer>

<script>
const observer=new IntersectionObserver((entries)=>{{entries.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('visible');observer.unobserve(e.target)}}}}}},{{{{"threshold":.15}}}});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
document.querySelectorAll('.nav a').forEach(a=>{{
  a.addEventListener('click',()=>{{document.querySelector('.nav').classList.remove('open')}});
}});
</script>
</body>
</html>'''
    return slug, html

# Generate all pages
os.makedirs("/tmp/nextlevel-marketing/locations", exist_ok=True)

count = 0
for county, cities in locations.items():
    for city, data in cities.items():
        slug, html = generate_page(city, data, county)
        filepath = f"/tmp/nextlevel-marketing/locations/{slug}.html"
        with open(filepath, "w") as f:
            f.write(html)
        count += 1
        print(f"Created: {slug}.html")

print(f"\nTotal pages created: {count}")
