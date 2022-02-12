//div[@class="movie-box row"]
//div[@id="HO00004296"]
//div[@class="movies-container"]/div
//div[@class="movies-container"]//div
//div[@id="HO00004296"]/..

//div[@class="movies-container"]/div[1]
//div[@class="movies-container"]/div[last()]
//div[@class="movies-container"]/div[last()-2]
//div[@class="movies-container"]/div[position()<3]

//div[@class="movies-container"]/div[1]//div[@class="movie-times" and a>1000]
//div[@class="movies-container"]/div[1]//div[@class="movie-times"][a>1000]

//div[@class="movies-container"]/div[1]//div[@class="movie-times"]//a[text()>1000]
//div[@class="movies-container"]/div[1]//div[@class="movie-times"]//a[text()="21:00"]

//div[@class="movies-container"]/div[1]//div[@class="movie-times"]//a[text()>1000 or text()="21:00"]


//div[@class="movies-container"]/div[1]/ancestor::div
//div[@class="movies-container"]/div[1]/ancestor::div[@class="row-promotions"]

//div[@class="movies-container"]/div[1]/descendant::div
//div[@class="movies-container"]/div[1]/descendant::div[@class="default-background center-background"]

//div[@class="movies-container"]/div[1]/parent::div
//div[@class="movies-container"]/div[1]/child::div

//div[@class="movies-container"]/div[1]/following::div
//div[@class="movies-container"]/div[1]/following::div[@class="movie-box row"]

//a[contains(text(), "SPIDERMAN")]
