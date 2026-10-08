# Nexscope Ecommerce API

Connect ecommerce workflows to marketplace data, product research, and AI image and video creation through Nexscope APIs.

**225 APIs · 172 Data APIs · 53 Creative APIs · 20 categories**

[Get an API key](https://www.nexscope.ai/seller/api-access?co-from=github-ecommerce-api) · [Official API docs](https://www.nexscope.ai/api-docs?co-from=github-ecommerce-api) · [Complete catalog](#complete-api-catalog) · [Integration guide](docs/calling-apis.md)

This repository includes documentation for every API in the official directory, request/response definitions, editable request samples, and cURL, JavaScript, and Python clients. Use it to connect marketplace research, sourcing, keyword analysis, product imagery, and video creation to your application.

## Quick start

### 1. Get and configure your API key

Open [API Access](https://www.nexscope.ai/seller/api-access?co-from=github-ecommerce-api), sign in, and create or copy your user API key. Send it in the `Authorization` header as a bearer token.

Creative API access requires an active subscription. Trial credits do not enable Creative API key access. Review your account access and [current plans](https://www.nexscope.ai/pricing?co-from=github-ecommerce-api) before submitting generation requests.

Keep the key on your server. Do not commit it or expose it in a browser application. In Bash or Zsh, enter it without displaying it or putting its value into shell history:

```bash
printf 'Nexscope API key: '
read -r -s NEXSCOPE_API_KEY
printf '\n'
export NEXSCOPE_API_KEY
```

All run requests use:

```http
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### 2. Make your first Data API request

This example calls [Amazon Search API](docs/data/amazon-search.md) for `phone case` results. It sends a real API request when you execute it with your key.

```bash
curl --silent --show-error --fail-with-body --max-time 120 \
  -X POST 'https://api.nexscope.ai/api/skill-api/v1/skills/amazon-search/run' \
  -H "Authorization: Bearer $NEXSCOPE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"keyword":"phone case","page":1}'
```

Response shapes vary by API; follow its current official reference. For [Amazon Product Detail](docs/data/amazon-product-detail.md#response), check `code === 0` and read business fields from `data` (for example, `data.products` and `data.total`); `data` may be null. The Amazon Search fixture below retains the original snapshot shape and should be verified against its current reference before integration. [Documented response fixture](examples/responses/amazon-search.json).

### 3. Use JavaScript, Python, or reusable cURL commands

Clone this repository and run commands from its root. The examples require Node.js 22+, Python 3.10+, or cURL 7.76+; the cURL helper also uses Python 3.10+ to look up and check the request. JavaScript and Python use only standard libraries.

```bash
git clone https://github.com/nexscope-ai/nexscope-ecommerce-api.git
cd nexscope-ecommerce-api

# Choose ONE client to submit a request:
node examples/javascript/run.mjs amazon-search payloads/amazon-search.json
# Alternatively:
python3 examples/python/run.py amazon-search payloads/amazon-search.json
# Alternatively:
bash examples/curl/run.sh amazon-search payloads/amazon-search.json
```

Each command above independently submits a request. To inspect the method, endpoint, and JSON without sending or using credits:

```bash
python3 examples/python/run.py amazon-search payloads/amazon-search.json --dry-run
node examples/javascript/run.mjs amazon-search payloads/amazon-search.json --dry-run
```

[JavaScript source](examples/javascript/run.mjs) · [Python source](examples/python/run.py) · [cURL source](examples/curl/run.sh)

### 4. Call a Creative API and retrieve its result

All 53 Creative APIs in this snapshot use asynchronous tasks. This example uses [Background Remover API](docs/creative/background-remover.md).

Create a request with **your real, publicly accessible image URL**. The input image must meet the API's documented limits, including 385–8192 pixels on both dimensions and a maximum size of 20 MB.

```bash
cp payloads/background-remover.json creative-request.json
# Edit creative-request.json: replace the example.com image URL with your asset URL.
# subType: 1 = general, 2 = portrait, 3 = product, 9 = apparel, 12 = hair, 13 = face.

python3 examples/python/run.py background-remover creative-request.json > creative-task.json
cat creative-task.json
```

The submission returns a receipt resembling this **illustrative documentation sample**:

```json
{
  "taskId": "6b3f1c61-1b7d-4a59-8a7d-3b23e4b0c9e2",
  "status": "PENDING",
  "message": "The task has been created. Use taskId to query the result."
}
```

Use the task ID returned by **your own request** to query the result; do not rerun the POST to check progress:

```bash
TASK_ID=$(python3 -c 'import json; print(json.load(open("creative-task.json"))["taskId"])')
python3 examples/python/run.py background-remover --task "$TASK_ID"
# Alternatively: node examples/javascript/run.mjs background-remover --task "$TASK_ID"
# Alternatively: bash examples/curl/run.sh background-remover --task "$TASK_ID"
```

The query endpoint is:

```http
GET https://api.nexscope.ai/api/skill-api/v1/skills/background-remover/tasks/{taskId}
Authorization: Bearer YOUR_API_KEY
```

- `PENDING` or `RUNNING`: the task is not complete. Query the same task later; a 5-second starting interval is an application recommendation, not an API rate-limit guarantee.
- `SUCCESS`: inspect the returned payload for generated outputs and the actual credits charged.
- `FAILED` or `TIMEOUT`: stop polling and inspect the error. A new submission is a separate request.

The included clients perform one submission or one status check per command. They do not automatically resubmit or poll indefinitely. See [asynchronous integration details](docs/calling-apis.md#asynchronous-creative-apis).

### 5. Switch to any API in the catalog

Open its documentation below, copy `payloads/<slug>.json` into your own request file, and replace illustrative inputs. Pass the slug and your file to the same client:

```bash
cp payloads/seedance-2-5-video-generation.json request.json
# Edit request.json with your real reference image and desired prompt.
python3 examples/python/run.py seedance-2-5-video-generation request.json
```

Parameter names, media requirements, conditional fields, and response shapes vary by API. The clients reject reserved example-domain asset URLs; you must also review sample product IDs, search terms, and other values for your intended use.

## Errors and response handling

| HTTP status | What to do |
|---|---|
| 200 | Follow the current response contract; when `code` is present, only `0` indicates business success or acceptance. For asynchronous work, also inspect the documented task status. |
| 400 | Check required fields, types, allowed values, conditional inputs, and media constraints. |
| 401 | Check the bearer header and API key. |
| 403 | Check account permissions, API access, and subscription requirements. |
| 429 | Respect `Retry-After` when present and back off. |
| 5xx | Inspect the service error. Before resubmitting a generation request, check whether a task was created. |

The helpers surface non-2xx responses and print the returned JSON. They do not currently reject nonzero platform `code` values; application code must perform that check when the endpoint uses the platform envelope. The Python and JavaScript helpers also exit with an error for `FAILED` or `TIMEOUT` task states; cURL reports HTTP status only. Do not blindly retry POST requests: the documentation does not establish an idempotency guarantee.

## Repository contents

| Path | Contents |
|---|---|
| [docs/data/](docs/data/) | 172 Data API references |
| [docs/creative/](docs/creative/) | 53 Creative API references |
| [catalog/apis.json](catalog/apis.json) | Complete inventory, categories, links, endpoints, and definition formats |
| [schemas/](schemas/) | 225 request and 225 response definitions |
| [payloads/](payloads/) | 225 published request samples |
| [examples/responses/](examples/responses/) | 225 published response fixtures |
| [examples/](examples/) | cURL, JavaScript, and Python clients for every catalog entry |
| [docs/calling-apis.md](docs/calling-apis.md) | Authentication, tasks, media, and MCP guidance |

## Complete API catalog

All 225 APIs listed in the official directory are included. Each entry links to its parameters, request/response definitions, sample payload, and official documentation.

### Data APIs — 172

#### Amazon Marketplace Intelligence (26)

| API | Purpose |
|---|---|
| [Amazon ASIN Traffic Summary API](docs/data/amazon-asin-traffic-summary.md) | Use SIF (Search Intelligence Framework) data to analyze ASIN traffic source composition and exposure distribution, covering current period/previous period/newly entered/exited period comparisons. |
| [Amazon Broad Product Search API](docs/data/amazon-broad-product-search.md) | Use SellerSprite data to search and filter Amazon products, supporting multi-dimensional criteria including price, monthly sales, BSR ranking, gross margin, ratings, fulfillment method, badges, seller origin, and more across multiple Amazon marketplaces. |
| [Amazon Category Lookup API](docs/data/amazon-category-lookup.md) | Browse Amazon category nodes or search category metadata by name. |
| [Amazon Competitor Lookup API](docs/data/amazon-competitor-lookup.md) | Use SellerSprite data to find and analyze competitors on Amazon, covering 12 marketplaces, with product metrics including sales, BSR, pricing, ratings, and growth trends. |
| [Amazon Market Product Detail API](docs/data/amazon-market-product-detail.md) | Query Amazon product detail and historical trends by ASIN using Sorftime data, covering 14 marketplaces. |
| [Amazon Market Product Search API](docs/data/amazon-market-product-search.md) | Multi-dimensional Amazon product search and filtering based on Sorftime data, covering 14 marketplaces, with support for historical monthly snapshot lookback. |
| [Amazon Market Research API](docs/data/amazon-market-research.md) | Use SellerSprite market list capability to filter Amazon niche markets by category dimensions, supporting market size, competition, top concentration, seller structure, new product share, price/rating/margin ranges, and many other criteria for discovering viable markets and evaluating product selection directions. |
| [Amazon Market Statistics API](docs/data/amazon-market-statistics.md) | Use SellerSprite market statistics capability to output a market statistics dashboard by category node, including top listing average rating, average price, BSR, sales, seller count, and new product related metrics, suitable for quickly assessing the market quality and competitive landscape of a category. |
| [Amazon Niche Info API](docs/data/amazon-niche-info.md) | Query and analyze Jiimore data for Amazon niche market insights, including market metrics, buyer reviews, competitive landscape, price trends, and growth trends. |
| [Amazon Niche Info By ASIN API](docs/data/amazon-niche-info-by-asin.md) | Deep analysis of Amazon niche markets by product ASIN, covering monopoly level, brand concentration, new product success rate, and market opportunity score. |
| [Amazon Opportunity Search By Metrics API](docs/data/amazon-opportunity-search-by-metrics.md) | Amazon reverse product selection: filter Amazon niches and keywords by 30+ business dimensions (market size & growth, price tiers & share, competition density & top concentration, demographics such as age/gender/income, review highlights & pain points) from a metrics pool aggregated from historical business insight reports. |
| [Amazon Policy Feed API](docs/data/amazon-policy-feed.md) | Query Amazon is latest policy, regulation, and compliance feed. Supports paginated browsing by marketplace and time range (with AI-generated Chinese summaries), and fetching full article body by record ID. |
| [Amazon Product Database API](docs/data/amazon-product-database.md) | Jungle Scout Product Database multi-condition filtering. Filter Amazon products by category, price, sales volume, revenue, reviews, rating, weight, BSR rank, LQS, seller type, and more across 10 marketplaces. |
| [Amazon Product Database Search API](docs/data/amazon-product-database-search.md) | Advanced Amazon product search and filtering powered by Keepa data, supporting multi-dimensional criteria including category, price, monthly sales, keywords, BSR rank, review count, rating, package dimensions, weight, fulfillment type, and more. |
| [Amazon Product Detail API](docs/data/amazon-product-detail.md) | Retrieve detailed Amazon product information by ASIN, including title, images, bullet points, specifications, A+ content, pricing, ratings & reviews, variants, and more. |
| [Amazon Product Discovery API](docs/data/amazon-product-discovery.md) | Amazon product discovery and potential bestseller mining via Jiimore data. |
| [Amazon Product History API](docs/data/amazon-product-history.md) | Retrieve Amazon product details by ASIN, including price, title, main image, listing date, material, weight, variant monthly sales, and up to 12 months of monthly sales history. |
| [Amazon Product Price Series API](docs/data/amazon-product-price-series.md) | Query Amazon product historical time-series data, including price trends, BSR (Best Sellers Rank) trends, rating changes, seller counts, and monthly sales, supporting any ASIN across multiple Amazon marketplaces. |
| [Amazon Product Research API](docs/data/amazon-product-research.md) | Browse the complete set of independently callable Amazon product-research APIs. |
| [Amazon Related ASINs API](docs/data/amazon-related-asins.md) | Find Amazon same-niche competitors by ASIN, with multi-dimensional filtering by click conversion rate, composite conversion rate, click volume, sales volume, reviews, ratings, price, and gross margin to identify potential competitors. |
| [Amazon Reviews List API](docs/data/amazon-reviews-list.md) | Fetch and analyze Amazon product reviews by ASIN, supporting 15 marketplaces (including US) with star rating filtering. |
| [Amazon Sales Estimates API](docs/data/amazon-sales-estimates.md) | Jungle Scout ASIN sales estimates query, returning daily estimated sales and latest known price for a specified ASIN over a given time period, covering 10 marketplaces including US, UK, Germany, and Japan. |
| [Amazon Search API](docs/data/amazon-search.md) | Simulates a real user searching on Amazon's storefront to get real-time keyword ranking and search results page data. |
| [Amazon Search By Image API](docs/data/amazon-search-by-image.md) | Perform image-based visual product search on Amazon across 8 marketplaces. Use an image URL to find visually similar products, with optional Keepa enrichment for sales data. |
| [Reverse Product Image Search API](docs/data/reverse-product-image-search.md) | Find visually similar Amazon products from a public image URL. |
| [Amazon Alexa Search API](docs/data/amazon-alexa-search.md) | Initiate natural language Q&A through Amazon's storefront Alexa shopping assistant to get shopping guidance answers, recommended product groups, ASIN lists, and follow-up questions. Each call supports only 1 prompt; for follow-ups, the agent must summarize context and concatenate a new question for a new request. A url can be used to supplement Amazon page context. |

#### Walmart Marketplace Intelligence (5)

| API | Purpose |
|---|---|
| [Walmart Category Market API](docs/data/walmart-category-market.md) | Walmart Category Market public data API. |
| [Walmart Keyword Research API](docs/data/walmart-keyword-research.md) | Walmart Keyword Research public data API. |
| [Walmart Product Analysis API](docs/data/walmart-product-analysis.md) | Walmart Product Analysis public data API. |
| [Walmart Product Detail API](docs/data/walmart-product-detail.md) | Query Walmart product details via WallySmarter, including pricing history and sales trends. |
| [Walmart Search API](docs/data/walmart-search.md) | Search and browse Walmart product listings by keyword, category, price range, and other conditions. |

#### Keyword & Search Demand (15)

| API | Purpose |
|---|---|
| [Amazon ASIN Keywords API](docs/data/amazon-asin-keywords.md) | Use SIF data to reverse-lookup traffic keywords for any Amazon ASIN, including organic ranking, ad ranking, search volume, traffic share, organic/paid scores, ABA TOP3 click concentration, click conversion rate, year-over-year search volume changes, and weekly/monthly time windows. |
| [Amazon Keyword Expansion API](docs/data/amazon-keyword-expansion.md) | Jungle Scout keyword expansion tool that expands a seed keyword into a list of related keywords with search volume, trends, PPC bids, ranking difficulty, and other metrics, covering 10 Amazon marketplaces including US, UK, DE, JP, etc. |
| [Amazon Keyword Intelligence API](docs/data/amazon-keyword-intelligence.md) | Query and analyze Amazon ABA (Brand Analytics) search term data, covering 15 marketplaces with nearly 3 years of weekly data. |
| [Amazon Keyword Overview API](docs/data/amazon-keyword-overview.md) | SIF overview analysis of Amazon keyword market competition. |
| [Amazon Keyword Search History API](docs/data/amazon-keyword-search-history.md) | Jungle Scout keyword historical search volume query, returning Amazon keyword exact search volume trends in 7-day periods, covering 10 marketplaces including US, UK, DE, JP, etc. |
| [Amazon Keyword Share Of Voice API](docs/data/amazon-keyword-share-of-voice.md) | Jungle Scout keyword Share of Voice analysis, returning brand visibility share across the first 3 pages of Amazon search results (organic/ad/combined), 30-day exact search volume, median PPC bid, and TOP3 ASIN click and conversion data, covering 10 marketplaces. |
| [Amazon Keyword Summary API](docs/data/amazon-keyword-summary.md) | Break down all competitor ASIN traffic sources under a given keyword -- organic search, SP ads, SB brand ads, SBV video ads, SP recommendations, AC/ER/TR recommendation slots, with support for ASIN filtering, custom date ranges, and new traffic keyword filters. |
| [Amazon Niche Info By Keyword API](docs/data/amazon-niche-info-by-keyword.md) | Deep analysis of Amazon niche markets by keyword, covering monopoly level, brand concentration, new product success rate, and market opportunity score. |
| [Amazon Niche Reviews By Keyword API](docs/data/amazon-niche-reviews-by-keyword.md) | Amazon niche market review analysis and consumer sentiment insights. |
| [Amazon Opportunity Report By Keyword API](docs/data/amazon-opportunity-report-by-keyword.md) | Query Amazon business insight reports by keyword, covering six dimensions: market potential, product characteristics, user reviews, customer profiles, search trends, and pricing analysis with AI-powered comprehensive analysis. |
| [Amazon Traffic Keywords API](docs/data/amazon-traffic-keywords.md) | Query traffic keyword lists for an Amazon ASIN via SellerSprite, including traffic source type, conversion type, organic rank, and ad rank with historical month and multi-dimensional sorting. |
| [Google Trends By Keywords API](docs/data/google-trends-by-keywords.md) | Google Trends keyword search popularity comparison and trend analysis, supporting global regions and custom time ranges. Triggered by: Google Trends, keyword popularity over time, search interest comparison, keyword trend analysis, seasonal trend detection, regional search popularity, keyword heatmap, multi-keyword comparison on Google, keyword research, market trend analysis, search trends, seasonal analysis, regional popularity. |
| [Ozon Keyword Back Search API](docs/data/ozon-keyword-back-search.md) | Seerfar Ozon keyword reverse lookup: reverse-looks up Ozon (and Wildberries) search keywords by a list of product SKUs (up to 20), returning which search terms those products appear under (organic/ad search terms), with multi-dimensional filtering by search volume, growth, product count, seller count, competitor count, natural rank, ad rank, exposure, conversion, cart-add conversion, etc. Each keyword carries monthly search volume, growth, market space, competitor/seller counts, average price, cart-add conversion, top products, and organic/ad channel, rank, exposure, and conversion (dimension) market profiles. Use for Ozon keyword reverse lookup, listing keyword optimization, competitor traffic word mining, and ad keyword analysis. |
| [Ozon Keyword Mining API](docs/data/ozon-keyword-mining.md) | Seerfar Ozon keyword mining: mines Ozon (and Wildberries) related keywords around a seed keyword with multi-dimensional filtering by search volume, growth, product count, seller count, competitor count, price, relevancy, title density, cart-add conversion, etc. Each mined keyword carries a full market profile (monthly search volume, growth, market space, competitor/seller counts, average price, cart-add conversion, top products). Use for Ozon keyword expansion, long-tail keyword mining, and seed keyword opportunity analysis. |
| [Ozon Market Keyword Search API](docs/data/ozon-market-keyword-search.md) | Seerfar Ozon market hot keyword search: filters Ozon (and Wildberries) market keywords by multi-dimensional metrics including search volume, growth, product count, seller count, competitor count, price, sales, conversion concentration, etc. Each keyword carries monthly search volume, growth, market space, competitor/seller counts, average price, cart-add conversion, top products, and market profile. Use for Ozon keyword selection, blue-ocean keyword mining, and market opportunity analysis. |

#### TikTok / Social Commerce (54)

| API | Purpose |
|---|---|
| [Chuhaijiang TikTok Product Search API](docs/data/chuhaijiang-tiktok-product-search.md) | Chuhaijiang TikTok Product Search with public market data. |
| [Chuhaijiang TikTok Product Detail API](docs/data/chuhaijiang-tiktok-product-detail.md) | Chuhaijiang TikTok Product Detail with public market data. |
| [Chuhaijiang TikTok Shop Detail API](docs/data/chuhaijiang-tiktok-shop-detail.md) | Chuhaijiang TikTok Shop Detail with public market data. |
| [Chuhaijiang TikTok Creator Detail API](docs/data/chuhaijiang-tiktok-creator-detail.md) | Chuhaijiang TikTok Creator Detail with public market data. |
| [Chuhaijiang TikTok Product Related Creators API](docs/data/chuhaijiang-tiktok-product-related-creators.md) | Chuhaijiang TikTok Product Related Creators with public market data. |
| [Chuhaijiang TikTok Product Related Lives API](docs/data/chuhaijiang-tiktok-product-related-lives.md) | Chuhaijiang TikTok Product Related Lives with public market data. |
| [Chuhaijiang TikTok Product Reviews API](docs/data/chuhaijiang-tiktok-product-reviews.md) | Chuhaijiang TikTok Product Reviews with public market data. |
| [Chuhaijiang TikTok Product Related Videos API](docs/data/chuhaijiang-tiktok-product-related-videos.md) | Chuhaijiang TikTok Product Related Videos with public market data. |
| [Chuhaijiang TikTok Shop Related Creators API](docs/data/chuhaijiang-tiktok-shop-related-creators.md) | Chuhaijiang TikTok Shop Related Creators with public market data. |
| [Chuhaijiang TikTok Shop Related Products API](docs/data/chuhaijiang-tiktok-shop-related-products.md) | Chuhaijiang TikTok Shop Related Products with public market data. |
| [Chuhaijiang TikTok Shop Related Videos API](docs/data/chuhaijiang-tiktok-shop-related-videos.md) | Chuhaijiang TikTok Shop Related Videos with public market data. |
| [Chuhaijiang TikTok Creator Related Lives API](docs/data/chuhaijiang-tiktok-creator-related-lives.md) | Chuhaijiang TikTok Creator Related Lives with public market data. |
| [Chuhaijiang TikTok Creator Related Products API](docs/data/chuhaijiang-tiktok-creator-related-products.md) | Chuhaijiang TikTok Creator Related Products with public market data. |
| [Chuhaijiang TikTok Creator Related Videos API](docs/data/chuhaijiang-tiktok-creator-related-videos.md) | Chuhaijiang TikTok Creator Related Videos with public market data. |
| [Chuhaijiang TikTok Product Most Promoted API](docs/data/chuhaijiang-tiktok-product-rankings-most-promoted.md) | Chuhaijiang TikTok Product Most Promoted with public market data. |
| [Chuhaijiang TikTok Product Top Selling API](docs/data/chuhaijiang-tiktok-product-rankings-top-selling.md) | Chuhaijiang TikTok Product Top Selling with public market data. |
| [Chuhaijiang TikTok Product New Arrivals API](docs/data/chuhaijiang-tiktok-product-rankings-new-arrivals.md) | Chuhaijiang TikTok Product New Arrivals with public market data. |
| [Chuhaijiang TikTok Product Image Search API](docs/data/chuhaijiang-tiktok-product-image-search.md) | Chuhaijiang TikTok Product Image Search with public market data. |
| [Chuhaijiang TikTok Shop Search API](docs/data/chuhaijiang-tiktok-shop-search.md) | Chuhaijiang TikTok Shop Search with public market data. |
| [Chuhaijiang TikTok Shop Most Promoted API](docs/data/chuhaijiang-tiktok-shop-rankings-most-promoted.md) | Chuhaijiang TikTok Shop Most Promoted with public market data. |
| [Chuhaijiang TikTok Shop Top Selling API](docs/data/chuhaijiang-tiktok-shop-rankings-top-selling.md) | Chuhaijiang TikTok Shop Top Selling with public market data. |
| [Chuhaijiang TikTok Creator Search API](docs/data/chuhaijiang-tiktok-creator-search.md) | Chuhaijiang TikTok Creator Search with public market data. |
| [Chuhaijiang TikTok Creator Agencies API](docs/data/chuhaijiang-tiktok-creator-rankings-agencies.md) | Chuhaijiang TikTok Creator Agencies with public market data. |
| [Chuhaijiang TikTok Creator Commercial API](docs/data/chuhaijiang-tiktok-creator-rankings-commercial.md) | Chuhaijiang TikTok Creator Commercial with public market data. |
| [Chuhaijiang TikTok Creator Growth API](docs/data/chuhaijiang-tiktok-creator-rankings-growth.md) | Chuhaijiang TikTok Creator Growth with public market data. |
| [Chuhaijiang TikTok Live Search API](docs/data/chuhaijiang-tiktok-live-search.md) | Chuhaijiang TikTok Live Search |
| [Chuhaijiang TikTok Live Detail API](docs/data/chuhaijiang-tiktok-live-detail.md) | Chuhaijiang TikTok Live Detail |
| [Chuhaijiang TikTok Live Related Products API](docs/data/chuhaijiang-tiktok-live-related-products.md) | Chuhaijiang TikTok Live Related Products |
| [Chuhaijiang TikTok Video Search API](docs/data/chuhaijiang-tiktok-video-search.md) | Chuhaijiang TikTok Video Search |
| [Chuhaijiang TikTok Video Detail API](docs/data/chuhaijiang-tiktok-video-detail.md) | Chuhaijiang TikTok Video Detail |
| [Chuhaijiang TikTok Video Related Products API](docs/data/chuhaijiang-tiktok-video-related-products.md) | Chuhaijiang TikTok Video Related Products |
| [Chuhaijiang TikTok Video Reviews API](docs/data/chuhaijiang-tiktok-video-reviews.md) | Chuhaijiang TikTok Video Reviews |
| [Chuhaijiang TikTok Ad Search API](docs/data/chuhaijiang-tiktok-ad-search.md) | Chuhaijiang TikTok Ad Search |
| [Chuhaijiang TikTok Ad Detail API](docs/data/chuhaijiang-tiktok-ad-detail.md) | Chuhaijiang TikTok Ad Detail |
| [Chuhaijiang TikTok Ad Related Products API](docs/data/chuhaijiang-tiktok-ad-related-products.md) | Chuhaijiang TikTok Ad Related Products |
| [Chuhaijiang TikTok Creative Search API](docs/data/chuhaijiang-tiktok-creative-search.md) | Chuhaijiang TikTok Creative Search |
| [Chuhaijiang TikTok Creative Detail API](docs/data/chuhaijiang-tiktok-creative-detail.md) | Chuhaijiang TikTok Creative Detail |
| [TikTok Video Rank API](docs/data/tiktok-video-rank.md) | TikTok Video Rank public data API. |
| [TikTok Shop Product Detail API](docs/data/tiktok-shop-product-detail.md) | TikTok Shop Product Detail public data API. |
| [TikTok Batch Product Detail API](docs/data/tiktok-batch-product-detail.md) | Batch query TikTok product detail data, including multi-period sales and GMV (1d/7d/15d/30d/60d/90d/cumulative), live sales and live GMV, promoting video and creator data, views, price, rating, review count, commission rate, and delisted/fully-managed status. Supports batch retrieval by product ID or TikTok Shop product URL. |
| [TikTok Creator Analytics API](docs/data/tiktok-creator-analytics.md) | Search TikTok e-commerce creator leaderboards via Kalodata and query detailed profiles for specific creators. Supports viewing top-performing influencer-sellers by region, currency, language, and date range, and using creatorId to retrieve follower count, video/live revenue and GPM, contact information, and associated shops. |
| [TikTok Creator Search API](docs/data/tiktok-creator-search.md) | Search TikTok ecommerce creator rankings. |
| [TikTok Livestream Analytics API](docs/data/tiktok-livestream-analytics.md) | Search TikTok e-commerce livestream leaderboards via Kalodata and query detailed data for specific livestreams. Supports viewing high-ranking, high-sales TikTok shopping livestreams by region, currency, language, and date range, and using livestreamId to retrieve revenue, viewers, duration, GPM, and number of products sold. |
| [TikTok New Product Rank API](docs/data/tiktok-new-product-rank.md) | Discover trending new products across 16 TikTok Shop regional markets via EchoTik new product ranking data. |
| [TikTok Product Analytics API](docs/data/tiktok-product-analytics.md) | Query TikTok e-commerce product leaderboards via Kalodata and query detailed data for specific products. Supports viewing high-ranking/hot-selling products by region, currency, language, and date range, and using productId to retrieve price range, sales, revenue, commission rate, listing/delisting time, and owning shop. |
| [TikTok Product Analytics Detail API](docs/data/tiktok-product-analytics-api.md) | Retrieve detailed performance data for a TikTok product. |
| [TikTok Product Discovery API](docs/data/tiktok-product-discovery.md) | Search and filter TikTok global e-commerce products based on FastMoss data, supporting keyword search, multi-dimensional filtering (category, shop type, commission rate, sales, creator count, etc.) and sorting. |
| [TikTok Product Search API](docs/data/tiktok-product-search.md) | Search and analyze TikTok product data including sales, influencer sales data, pricing, and commission rates across 16 TikTok Shop sites. |
| [TikTok Seller Detail API](docs/data/tiktok-seller-detail.md) | Query TikTok Shop store (seller) details, retrieving a complete store profile by sellerId with total sales, multi-period (1d/7d/30d/90d) sales and GMV, followers, rating, review count, positive feedback rate, delivery rate, response rate, in-store product count, promoting creator count, promotional video count, livestream count, price range, product categories, and estimated listing time. |
| [TikTok Shop Analytics API](docs/data/tiktok-shop-analytics.md) | Search TikTok e-commerce store leaderboards via Kalodata and query detailed information for specific stores. Supports viewing high-ranking, high-sales TikTok Shop stores by region, currency, language, and date range, and using shopId to retrieve revenue, sales volume, on-sale product count, self-operated/affiliate/shopping mall channel revenue, and creator collaboration count. |
| [TikTok Top Selling Products API](docs/data/tiktok-top-selling-products.md) | Query TikTok global e-commerce market top-selling product rankings via FastMoss data, supporting daily/weekly/monthly dimensions and category-level analysis. |
| [TikTok Video Analytics API](docs/data/tiktok-video-analytics.md) | Search TikTok e-commerce trending promotional video leaderboards via Kalodata and query detailed data for specific videos. Supports viewing high-ranking/high-view/hot-selling promotional videos by region, currency, language, and date range, and using videoId to retrieve views, likes, comments, shares, revenue, GPM, and advertising metrics. |
| [TikTok Video Download URL API](docs/data/tiktok-video-download-url.md) | Resolve TikTok video URLs to return no-watermark/watermarked download addresses, playback addresses, and cover image addresses for saving promotional video assets or offline analysis. |
| [TikTok Video Search API](docs/data/tiktok-video-search.md) | Search and analyze TikTok video data, filter videos by region, creator, product, category, views, duration, publish time, selling/ad/AI video flags, and return views, likes, comments, shares, favorites, video sales and GMV metrics across 16 TikTok Shop sites. |

#### Temu Marketplace Intelligence (11)

| API | Purpose |
|---|---|
| [GeekBI Temu Site List API](docs/data/geekbi-temu-site-list.md) | List Temu site records. |
| [GeekBI Temu Category Research API](docs/data/geekbi-temu-category-search.md) | Category Research using GeekBI Temu data. |
| [GeekBI Temu Keyword Research API](docs/data/geekbi-temu-keyword-search.md) | Keyword Research using GeekBI Temu data. |
| [GeekBI Temu Product Search API](docs/data/geekbi-temu-goods-search.md) | Product Search using GeekBI Temu data. |
| [GeekBI Temu Product Detail API](docs/data/geekbi-temu-goods-detail.md) | Product Detail using GeekBI Temu data. |
| [GeekBI Temu Shop Search API](docs/data/geekbi-temu-mall-search.md) | Shop Search using GeekBI Temu data. |
| [GeekBI Temu Image Search API](docs/data/geekbi-temu-goods-image-search.md) | Image Search using GeekBI Temu data. |
| [GeekBI Temu Category List API](docs/data/geekbi-temu-category-list.md) | List Temu category records. |
| [Temu Category Search API](docs/data/temu-category-search.md) | Search synced Temu category data in the local database by keyword to find category Chinese names, English names, and category IDs for use in product/store filtering. |
| [Temu Product Source Query API](docs/data/temu-product-source-query.md) | Filter Temu products by multiple dimensions (keyword/product ID/store ID, front/backend categories, price, rating, reviews, total/weekly/daily sales, listing date, fully-managed/semi-managed, semi-managed regions, tags, etc.). |
| [Temu Store Source Query API](docs/data/temu-store-source-query.md) | Filter Temu stores by multiple dimensions (store name/ID, country site, backend category, fully-managed/semi-managed, total/weekly/monthly sales and revenue, rating, reviews, followers, product count, store opening time, etc.). |

#### 1688 Sourcing (4)

| API | Purpose |
|---|---|
| [1688 Product Detail API](docs/data/1688-product-detail.md) | 1688 Product Detail public data API. |
| [1688 Product Billboard API](docs/data/1688-product-billboard.md) | Query 1688 product bestseller billboard data for sourcing discovery and wholesale product research. |
| [1688 Product Search API](docs/data/1688-product-search.md) | Search and analyze products on the Chinese 1688 wholesale platform (Alibaba domestic B2B market) for sourcing, supplier discovery, and product selection. |
| [1688 Search By Image API](docs/data/1688-search-by-image.md) | Perform image-based product search on the 1688 platform. Use an image URL to find visually similar supplier products, returning title, price, minimum order quantity, monthly sales, repurchase rate, trade score, and seller identity. |

#### Shopify Commerce (2)

| API | Purpose |
|---|---|
| [Shopify Product Query API](docs/data/shopify-product-query.md) | Filter Shopify standalone store products by multiple dimensions (keyword/URL, price, weekly sales, listing date, Facebook ads, competitiveness, supplier availability, shipping country, etc.). |
| [Shopify Store Query API](docs/data/shopify-store-query.md) | Filter Shopify standalone stores by multiple dimensions (store name/domain, country, years since creation, product count, ad count, monthly visits, monthly orders, social media followers, etc.). |

#### Etsy Marketplace (4)

| API | Purpose |
|---|---|
| [Etsy Product Detail API](docs/data/etsy-product-detail.md) | Etsy Product Detail public data API. |
| [Etsy Category Search API](docs/data/etsy-category-search.md) | Search Etsy category data by name, ID, or parent IDs to find category identifiers for product/store filtering. |
| [Etsy Product Query API](docs/data/etsy-product-query.md) | Query Etsy products with multi-dimensional filters (keyword/URL, price, sales, favorites, reviews, listing date, category, handmade/vintage types, Pick/Bestseller/Raving tags). |
| [Etsy Store Query API](docs/data/etsy-store-query.md) | Search Etsy stores using keyword, category, country, status, performance, and date filters. |

#### Ozon Marketplace (10)

| API | Purpose |
|---|---|
| [Ozon Brand Products API](docs/data/ozon-brand-products.md) | MPSTATS Ozon Russia brand drill-down product list. Returns all products under an Ozon brand display name (Russian/Latin) with complete metrics: sales, revenue, price, rating, stock, turnover, lost revenue, supporting multi-dimensional numeric filters, sorting, and currency conversion. Use for brand benchmarking, competitor analysis, brand product structure research, SKU-level bestseller analysis. |
| [Ozon Category Products API](docs/data/ozon-category-products.md) | MPSTATS Ozon Russia category drill-down product list by Russian category path. Returns all products in a category with complete metrics: sales, revenue, price, rating, stock, turnover, lost revenue, supporting multi-dimensional numeric filters, sorting, and currency conversion. Use for category bestseller mining, blue-ocean insight discovery, category ranking analysis, brand landscape observation. |
| [Ozon Category Search API](docs/data/ozon-category-search.md) | Seerfar Ozon category product search: fetches the product list for a given Ozon category ID, returning category-level aggregates (total sales, total revenue, average price, average rating, seasonality) and per-product sales, price, rating, review count, brand, seller, and fulfillment method. Use for category selection analysis, category bestseller mining, category capacity and price band analysis, seasonality assessment. |
| [Ozon Product Detail API](docs/data/ozon-product-detail.md) | MPSTATS Ozon Russia SKU full detail query for one product ID per call, returning price, discount, Ozon Card price, rating, review count, stock, sales, revenue, revenue potential/lost revenue, listing date, images, and the complete product card. |
| [Ozon Product Detail Search API](docs/data/ozon-product-detail-search.md) | Seerfar Ozon product detail query: fetches the complete detail of a single Ozon product by SKU, returning title, price (RUB), rating, review count, QA count, total and daily average sales within the stats window, revenue, stock, category ranking, daily sales trend, brand, seller, fulfillment method (FBO/FBS/OZON), weight, and listing time/days/months. Use for single product deep analysis, competitor product teardown, Ozon product selection assessment, listing diagnosis, sales trend and category ranking tracking. |
| [Ozon Product Report Search API](docs/data/ozon-product-report-search.md) | Seerfar Ozon product report search: filters Ozon products by multi-dimensional metrics including sales, revenue, sales/revenue growth rate, cart conversion rate, order conversion rate, price, rating, review count, QA count, variant count, page views, gross margin, return/cancellation rate, ad spend share, weight/volume, listing time, brand, seller, fulfillment method, and labels. Returns each product's SKU, title, price (RUB), sales, revenue, lost revenue, conversion rate, rating, reviews, brand, seller, fulfillment method, listing days/months, and complete product report fields. Use for Ozon product selection, competitor product analysis, best-seller mining, price/conversion band filtering. |
| [Ozon Product Search API](docs/data/ozon-product-search.md) | MPSTATS Ozon Russia product search and reverse lookup. Searches Ozon products in the MPSTATS database by Russian keyword or SKU, returning product ID, title, brand, and seller information. The entry point for Ozon product discovery and competitor analysis chains. |
| [Ozon Product Trend API](docs/data/ozon-product-trend.md) | MPSTATS Ozon Russia single SKU daily time-series performance. Returns daily sales units, price, stock, rating, and optionally search position/visibility data for one Ozon product by date granularity. Use for validating growth trends, seasonality, and anomaly detection. |
| [Ozon Seller Products API](docs/data/ozon-seller-products.md) | MPSTATS Ozon Russia seller drill-down product list by seller ID. Returns all SKUs under a seller with complete metrics: sales, revenue, price, rating, stock, turnover, lost revenue, supporting multi-dimensional numeric filters, sorting, and currency conversion. Use for store structure analysis, seller bestseller analysis, competitor store benchmarking. |
| [Ozon Shop Search API](docs/data/ozon-shop-search.md) | Seerfar Ozon shop product search: fetches the product list of an Ozon shop (seller) by shop ID, returning each product's 30-day sales, price, rating, weight, fulfillment method (FBO/FBS), seller type (local/cross-border), return/cancellation rate, and the shop's total 30-day sales. Use for competitor shop product analysis, shop bestseller mining, seller product structure analysis. |

#### eBay Marketplace (1)

| API | Purpose |
|---|---|
| [eBay Search API](docs/data/ebay-search.md) | Search and browse product listings across multiple eBay international sites. |

#### Shopee Marketplace (2)

| API | Purpose |
|---|---|
| [Shopee Product Detail API](docs/data/shopee-product-detail.md) | Shopee Product Detail public data API. |
| [Shopee Product Search API](docs/data/shopee-product-search.md) | YouYing Shopee product selection tool supporting product query and filtering across all Shopee marketplaces, covering Malaysia, Taiwan (China), Indonesia, Thailand, Philippines, Singapore, Vietnam, Brazil, Mexico, Chile, and Colombia. |

#### Search & Trend Intelligence (3)

| API | Purpose |
|---|---|
| [Google AI Mode Search API](docs/data/google-ai-mode-search.md) | AI Overview (AI Mode) scraping via Google Search. Returns AI-summarized key points for a single keyword, ideal for deep research, technical Q&A, long-tail product selection, and cross-border consumer preference analysis using the latest web information. Single-round only; follow-ups require the agent to summarize context and issue a new request. Triggered by: Google AI, AI Overview, AI Mode, Google AI search, AI search, deep research, consumer preference analysis, web summary, long-tail product research, cross-border market insights. |
| [Google Trends By Time API](docs/data/google-trends-by-time.md) | Query and analyze Google Trends real-time hot topics and trending searches for a specified time range and country/region. Triggered by: Google Trends, hot topics, real-time trending, popular trends, current hot searches, recent trending, viral topics, trending searches, trend discovery, market trends, what's popular, trending now, breakout topics. |
| [Web Search API](docs/data/web-search.md) | Web search, online retrieval, real-time information query, search engine search, Reddit and other community platform discussions, external site posts and trending topics. |

#### AI Content Generation (1)

| API | Purpose |
|---|---|
| [Product Description Generator API](docs/data/product-description-generator.md) | Create or query asynchronous product-description generation tasks. |

#### Patent & IP Risk (23)

| API | Purpose |
|---|---|
| [Google Patent Search API](docs/data/google-patent-search.md) | Google Patent Search public data API. |
| [Product TRO Detection API](docs/data/maidalv-product-tro-detection.md) | Assess product imagery for TRO, trademark, patent, and copyright infringement risk. |
| [Patent Abstract Image Data API](docs/data/patent-abstract-image-data.md) | Retrieves patent abstract images (drawings) from the Zhihuiya (PatSnap) patent database by patent ID or publication number. |
| [Patent Cited By API](docs/data/patent-cited-by.md) | Retrieve patents that cite one or more PatSnap patents. |
| [Patent Claims API](docs/data/patent-claims.md) | Retrieves patent claims data from Zhihuiya (PatSnap). |
| [Patent Claims Translation API](docs/data/patent-claims-translation.md) | Retrieves translated patent claims from the Zhihuiya (PatSnap) patent database. |
| [Patent Core Bibliography API](docs/data/patent-core-bibliography.md) | Retrieve core bibliographic records for one or more patents. |
| [Patent Description Data API](docs/data/patent-description-data.md) | Retrieve patent description (specification) data from the Zhihuiya patent database by patent ID or publication number. |
| [Patent Description Data Translation API](docs/data/patent-description-data-translation.md) | Retrieve translated patent description (specification) text from Zhihuiya. |
| [Patent Detailed Bibliography API](docs/data/patent-detailed-bibliography.md) | Query patent bibliographic (catalog) information from the Zhihuiya patent database by patent ID or publication number. |
| [Patent Fulltext Images API](docs/data/patent-fulltext-images.md) | Retrieve fulltext images (drawings, diagrams, charts) from patent documents by patent ID or publication number. |
| [Patent Family Data API](docs/data/patent-family-data.md) | Retrieve simple, INPADOC, and PatSnap patent family records. |
| [Patent Legal Status Data API](docs/data/patent-legal-status-data.md) | Query patent legal status information from the Zhihuiya (PatSnap) database. |
| [Patent References API](docs/data/patent-references.md) | Retrieve patent and non-patent references cited by one or more patents. |
| [Patent Title Abstract Translation API](docs/data/patent-title-abstract-translation.md) | Retrieve translated patent titles and abstracts from the Zhihuiya (PatSnap) patent database. |
| [Ruiguan Copyright Detection API](docs/data/ruiguan-copyright-detection.md) | Detect image copyright infringement risks by comparing against a database of registered copyrighted works with similarity scoring, TRO litigation history, and radar-based infringement assessment. |
| [Ruiguan Detection Patent Design API](docs/data/ruiguan-detection-patent-design.md) | Detect design patent infringement risks by comparing a product image against a global design patent database across 25+ jurisdictions. |
| [Ruiguan Gun Parts Search API](docs/data/ruiguan-gun-parts-search.md) | Check product images against a database of policy-violating items using visual similarity matching. |
| [Ruiguan Trademark Graphic Detection API](docs/data/ruiguan-trademark-graphic-detection.md) | Detect graphic trademarks in product images by comparing against registered trademark databases across 15 major trademark offices using YOLO-based object detection and visual similarity. |
| [Text Trademark Detector API](docs/data/text-trademark-detector.md) | Text trademark detection and infringement risk analysis for e-commerce product listings. |
| [Utility Patent Detector API](docs/data/utility-patent-detector.md) | Detect and search for similar utility/invention patents based on product information. |
| [Zhihuiya Patent Image Search API](docs/data/zhihuiya-patent-image-search.md) | Perform visual similarity search for design patents using an image URL, with filtering by country, legal status, date ranges, Locarno classification, and assignee. Supports design patent types only (type D). |
| [Zhihuiya Utility Patent Image Search API](docs/data/zhihuiya-utility-patent-image-search.md) | Perform visual similarity search for utility model patents using an image URL, with filtering by country, legal status, date ranges, and assignee. Supports utility model patents only (type U) with shape-only or shape+pattern+color matching models. |

#### Product & Market Research (2)

| API | Purpose |
|---|---|
| [Mercado Market Intelligence API](docs/data/mercado-market-intelligence.md) | Mercado Market Intelligence public data API. |
| [Mercado Product Selection API](docs/data/mercado-product-selection.md) | Run one of 24 documented Mercado Libre product, category, trend, seller, review, rate, or usage tools. |

#### Amazon Advertising (8)

| API | Purpose |
|---|---|
| [Amazon Ads SP Audience Report API](docs/data/amazon-ads-sp-audience-report.md) | Amazon Ads SP Audience Report using an owned Amazon Ads connection. |
| [Amazon Ads SP Search Impression Share Report API](docs/data/amazon-ads-sp-search-impression-share-report.md) | Amazon Ads SP Search Impression Share Report using an owned Amazon Ads connection. |
| [Amazon Ads SP Insights Report Status API](docs/data/amazon-ads-sp-insights-report-status.md) | Amazon Ads SP Insights Report Status using an owned Amazon Ads connection. |
| [Amazon Ads SP Insights Report Download API](docs/data/amazon-ads-sp-insights-report-download.md) | Amazon Ads SP Insights Report Download using an owned Amazon Ads connection. |
| [Amazon Ads Manager API](docs/data/amazon-ads-manager.md) | Run a catalogued Amazon Ads entity operation. |
| [Amazon Ads API Access](docs/data/amazon-ads-api-access.md) | Authorize Amazon Ads and inspect owned connections and profiles. |
| [Amazon Ads Reporting API](docs/data/amazon-ads-reporting.md) | Create, poll, and download governed Amazon Ads reports. |
| [Amazon Advertising API](docs/data/amazon-advertising.md) | Run a catalogued Amazon Ads entity operation. |

#### Patent Intelligence (1)

| API | Purpose |
|---|---|
| [Patent Search API](docs/data/patent-search.md) | Search patent publications with an Analytics query expression. |

### Creative APIs — 53

#### Image Generation Models (7)

| API | Purpose |
|---|---|
| [Nano Banana Image Generation](docs/creative/banana-image-generation.md) | Generate ecommerce images with the BANANA model. |
| [Nano Banana Pro Image Generation](docs/creative/banana-pro-image-generation.md) | Generate ecommerce images with the BANANA_PRO model. |
| [Nano Banana 2 Image Generation](docs/creative/banana-2-image-generation.md) | Generate ecommerce images with the BANANA_2 model. |
| [Nano Banana 2 Lite Image Generation](docs/creative/banana-2-lite-image-generation.md) | Generate ecommerce images with the BANANA_2_LITE model. |
| [Wan 2.7 Image Generation](docs/creative/wan-2-7-image-generation.md) | Generate ecommerce images with the WAN2_7 model. |
| [Seedream 5 Pro Image Generation](docs/creative/seedream-5-pro-image-generation.md) | Generate ecommerce images with the SEEDREAM5_PRO model. |
| [GPT Image 2 Generation](docs/creative/gpt-image-2-generation.md) | Generate ecommerce images with the GPT_2_IMAGE model. |

#### Video Generation Models (12)

| API | Purpose |
|---|---|
| [Seedance 2.0 Video Generation](docs/creative/seedance-2-0-video-generation.md) | Generate ecommerce videos with the seedance-2-0 model. |
| [Seedance 2.0 Fast Video Generation](docs/creative/seedance-2-0-fast-video-generation.md) | Generate ecommerce videos with the seedance-2-0-fast model. |
| [Seedance 2.0 Mini Video Generation](docs/creative/seedance-2-0-mini-video-generation.md) | Generate ecommerce videos with the seedance-2-0-mini model. |
| [Seedance 2.5 Video Generation](docs/creative/seedance-2-5-video-generation.md) | Generate ecommerce videos with the seedance-2-5 model. |
| [Kling 2.6 Video Generation](docs/creative/kling-2-6-video-generation.md) | Generate ecommerce videos with the kling-v2-6 model. |
| [Kling 3 Omni Video Generation](docs/creative/kling-3-omni-video-generation.md) | Generate ecommerce videos with the kling-v3-omni model. |
| [Wan 2.6 Video Generation](docs/creative/wan-2-6-video-generation.md) | Generate ecommerce videos with the wan-2-6 model. |
| [Hailuo 2.3 Video Generation](docs/creative/hailuo-2-3-video-generation.md) | Generate ecommerce videos with the hailuo-2-3 model. |
| [Happy Horse 2 Video Generation](docs/creative/happy-horse-2-video-generation.md) | Generate ecommerce videos with the happyhorse-v2 model. |
| [Wan 3 Video Generation](docs/creative/wan-3-video-generation.md) | Generate ecommerce videos with the wan3 model. |
| [MiniMax H3 Video Generation](docs/creative/minimax-h3-video-generation.md) | Generate ecommerce videos with the minimax-h3 model. |
| [MiniMax H3 Lite Video Generation](docs/creative/minimax-h3-lite-video-generation.md) | Generate ecommerce videos with the minimax-h3-lite model. |

#### Multimodal AI (34)

| API | Purpose |
|---|---|
| [AI Model Swap API](docs/creative/ai-model-swap.md) | Swap an ecommerce product image onto a target model. |
| [AI Model Swap API 2.0](docs/creative/ai-model-swap-2-0.md) | Swap a product image onto a fixed model reference. |
| [AI Model Scene & Background Replacement API](docs/creative/ai-model-scene-background-replacement.md) | Place a model image into a new scene. |
| [AI Clothes Changer API for Tops & Bottoms](docs/creative/ai-clothes-changer-for-tops-bottoms.md) | Generate try-on images for separate upper and lower garments. |
| [AI Suit Virtual Try-On API](docs/creative/ai-suit-virtual-try-on.md) | Generate try-on images for one-piece outfits. |
| [Virtual Try-On API](docs/creative/virtual-try-on.md) | Place a product naturally onto a person or model image. |
| [Product Replacement API](docs/creative/product-replacement.md) | Replace a product region in an ecommerce image. |
| [Product Scene Variations API](docs/creative/product-scene-variations.md) | Create scene variations from an image. |
| [AI Background Generator API](docs/creative/ai-background-generator.md) | Generate an ecommerce scene image from a prompt. |
| [Similar Image Variations API](docs/creative/similar-image-variations.md) | Create similar image variations. |
| [Background Remover API](docs/creative/background-remover.md) | Automatically remove image background. |
| [Fine Cutout Image Segmentation API](docs/creative/fine-cutout-image-segmentation.md) | Create a fine cutout task and return the completed result. |
| [Image Upscale API](docs/creative/image-upscale.md) | Upscale and enhance an image. |
| [Smart Image Outpainting API](docs/creative/smart-image-outpainting.md) | Expand an image canvas with AI. |
| [Image Translation API](docs/creative/image-translation.md) | Translate text inside an image. |
| [AI Hand Repair API](docs/creative/ai-hand-repair.md) | Repair distorted hands in an image. |
| [Image Inpainting API](docs/creative/image-inpainting.md) | Redraw a masked image area. |
| [Print & Pattern Extraction API](docs/creative/print-pattern-extraction.md) | Extract printed artwork from an image. |
| [Object Eraser & Image Object Removal API](docs/creative/object-eraser-image-object-removal.md) | Erase masked objects from an image. |
| [Jewelry Text Design API](docs/creative/jewelry-text-design.md) | Generate linked text for jewelry or accessory designs. |
| [Handheld Product Mockup API](docs/creative/handheld-product-mockup.md) | Place a product in a hand-held scene. |
| [Image Captioning API](docs/creative/image-captioning.md) | Create an image prompt extraction task and return the completed result. |
| [Product Image Enhancement API](docs/creative/product-image-enhancement.md) | Retouch a product image. |
| [Image Text Editing API](docs/creative/image-text-editing.md) | Remove or edit text from an image. |
| [Smart Image Edit & Manipulation API v3](docs/creative/smart-image-edit-manipulation-v3.md) | Edit an image using an instruction prompt. |
| [Smart Multi-Image Editing API v3](docs/creative/smart-multi-image-editing-v3.md) | Fuse multiple images with an instruction prompt. |
| [White Background Product Image API](docs/creative/whitebg-image.md) | Generate a square white-background product image from reference photos. |
| [AI Video Reclone API](docs/creative/ai-video-reclone.md) | Recreate a product marketing video from references. |
| [AI Product Marketing Image Set API v4](docs/creative/ai-product-marketing-image-set-v4.md) | Generate product marketing image sets. |
| [AI Apparel Image Set & Photography API v3](docs/creative/ai-apparel-image-set-photography-v3.md) | Generate apparel marketing image sets. |
| [AI Model Pose Generation API](docs/creative/ai-model-pose-generation.md) | Create new pose variants for a model image. |
| [Sales Talking Video API](docs/creative/sales-talking-video.md) | Generate a talking sales video. |
| [Product Logo Detection & Removal API](docs/creative/product-logo-detection-removal.md) | Detect and remove product logos. |
| [One-Click Image Recoloring API v2](docs/creative/one-click-image-recoloring-v2.md) | Change product colors in an image. |

## Source, coverage, and validation

Snapshot: **2026-09-10**, from the [official API directory](https://www.nexscope.ai/api-docs?co-from=github-ecommerce-api) and its public definition service. Counts refer to documented API entries, not every supporting HTTP route. The complete 225-entry inventory is included; live documentation can change after this snapshot.

Some definitions use field descriptors rather than standard JSON Schema. Each format is labeled in the catalog. Published request and response samples are illustrative fixtures, not evidence of successful live calls. No authenticated or billable API requests were executed to prepare this repository. See [source notes](docs/source-notes.md) for the precise validation scope.

Run the offline consistency checks:

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
node --check examples/javascript/run.mjs
bash -n examples/curl/run.sh
```

## Contributing and license

For a documentation correction, include the API slug and relevant official documentation link. Never include API keys, account data, or private request logs.

Example code, validation scripts, tests, and workflow configuration are provided under the MIT terms in [LICENSE](LICENSE). API documentation, catalog content, definitions, and sample data remain copyright Nexscope; no separate open-content license is granted here. API service use remains subject to Nexscope's applicable terms and account access requirements.
