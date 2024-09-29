let btn = document.getElementById("shorten");

btn.addEventListener('click', short);


async function short(){
    let longURL = document.getElementById("longurl").value;
    let shortURL = document.getElementById("shorturl");

    const result = await fetch(`https://link-shortener-backend-r2jzsirr4-nasheeths-projects.vercel.app/${shortURL.value}`);
    const data = await result.json();

    shortURL.value = data["url"]
}
