# Session 2 - APIs

## 0. Send Emails
**🔎 Goal:** Send an email to yourself.

> Using [google app password](https://myaccount.google.com/apppasswords) (requires enabling 2FA)

---

## 1. Quotable API
**🔎 Goal:** Get a random quote from quotable.io

> No registration, free

---

## 2. Wikipedia API
**🔎 Goal:** Get the first 3 sentences of a Wikipedia page

> No registration, free

---

## 3. Weather API
**🔎 Goal:** Get the weather from a city

> [Open Weather Map](https://openweathermap.org/current) (registration, free)

---

## 4. Google Search Results
**🔎 Goal:** Save the first 10 results of a google search

> [SerpAPI](https://serpapi.com/) (registration, free)

---

## 5. OpenAI Text Generation
**🔎 Goal:** Generate text with ChatGPT

> [OpenAI API](https://platform.openai.com/docs/overview) (registration, paid)

**🔎 Additional Goal:** Modify the code to count tokens and evaluate the cost of each request to OpenAI

> Check the [pricing](https://openai.com/api/pricing) if need be

---

## 6. OpenAI Image Generation
**🔎 Goal:** Generate an image with ChatGPT

> [OpenAI API](https://platform.openai.com/docs/overview) (registration, paid)

---

## 7. OpenAI Image Description
**🔎 Goal:** Ask ChatGPT to describe the image you generated

> [OpenAI API](https://platform.openai.com/docs/overview) (registration, paid)

**🔎 Additional Goal:** Find if an image is real or AI-generated

---

## 8. Waves Forecast
**🔎 Goal:** Find the height of waves in Nazare this week

> [WorldWeatherOnline](https://www.worldweatheronline.com/) (registration, free)

---

## 9. Open Movie Database
**🔎 Goal:** Ask the user for a movie title and let them guess the release year

> [OMDB API](https://www.omdbapi.com/) (registration, free)

**🔎 Additional Goal:** Show three fun facts about a movie (genre, actors, awards)

**🔎 Additional Goal:** Ask the user for a movie title and tell how many Oscars it has won

---

## 10. Update a Sheet
**🔎 Goal:** Post data from data.csv to google sheet using the Google Sheets API

> Registration, free

### Guide to Setting Up Google Sheets API

#### Step 1: Enable the Google Sheets API
1. Go to the Google Cloud Console.
2. Click in `Console` on the header
3. Create a project (to the right of the "Google Cloud" logo).
4. Search for `Google Sheets API`.
5. Click it, then click `Enable`.

#### Step 2: Create a Service Account
1. Go to `IAM & Admin` → `Service Accounts`.
2. Click `Create Service Account`.
3. Give it a name (e.g., `sheets-writer`), then click `Create and Continue`.
4. Skip assigning a role (you'll give access by sharing the sheet).
5. Click `Done`.

#### Step 3: Create and Download a JSON Key
1. In the list of service accounts, click the 3 dots next to your new account.
2. Click `Manage keys`.
3. Under `Keys`, click `Add Key` → `Create new key`.
4. Select `JSON`, then click `Create`.
5. Save the `.json` file securely. You'll use this in your Python code.

> **Note:** JSON (JavaScript Object Notation) is a type of file used for storing and exchanging data between applications.

#### Step 4: Share Your Sheet with the Service Account
1. Open the Google Sheet you want to access.
2. Click `Share` in the top-right.
3. Add the service account email (e.g., `sheets-writer@your-project.iam.gserviceaccount.com`) with `Editor` permission.
4. Click `Send`.

**Example Information:**
- **Service Account Email:** `sheets-writer@vibe-coding-course-465513.iam.gserviceaccount.com`
- **JSON Key File:** `vibe-coding-course-465513-08606c73d1c9.json`
- **Sheet URL:** `https://docs.google.com/spreadsheets/d/175afjIAecFc9ahwjuypqFtsNu62U0k9WAF0PYPCxT00/edit?usp=sharing`

#### Step 5: Task - Extract Spreadsheet ID
1. From the sheet URL, identify and extract the spreadsheet ID.
2. For the example URL, the ID is `175afjIAecFc9ahwjuypqFtsNu62U0k9WAF0PYPCxT00`.

#### Step 6: Task - Update the Sheet
1. Replace some cells in the sheet with the following data:

```
Name,Age
Alice,30
Bob,25
```
