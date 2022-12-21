
# App Store Review Scrapper

A simple Python script to gather reviws from an application from Apple's App Store and save it's reviews to a ``.csv`` file.


## Run locally

Clone the project

```bash
  git clone https://github.com/aerodiduch/review-scrapper
```

Go to the project directory

```bash
  cd review-scrapper
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Now, inside `main.py` you have to specify three variables

- App country
- App full name
- App id

These three items can be found by simply reading the app's app store link. For example, in Slack URL:

`https://apps.apple.com/us/app/slack/id618783545`

We can identify that country is `us`, full name is `slack` and id is `618783545`

Sometimes apps might have a longer name including dashes, that's ok. `my-super-long-app-name` is as valid as `foo`.

Then, simply run the script and results will be dumped to a `.csv` in the current directory.

```bash
  python main.py
```

```
2022-12-21 02:22:46,683 [INFO] Base - Initialised: AppStore('country', 'name', appId)
2022-12-21 02:22:46,683 [INFO] Base - Ready to fetch reviews from: ...
```