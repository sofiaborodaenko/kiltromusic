export function loadNav() {
  const nav = `
  <nav>
      <div class="dropdown">
        <button class="averia-libre-regular">menu</button>
        <div class="content">
        <a class="averia-libre-regular" href="index.html">home</a>
          <a class="averia-libre-regular" href="music.html">music</a>
          <a class="averia-libre-regular" href="">live events</a>
          <a class="averia-libre-regular" href="">our story</a>
          <a
            class="averia-libre-regular"
            href="https://kiltro-music.myshopify.com/"
            target="_blank"
            >shop</a
          >
          <a class="averia-libre-regular" href="index.html#contact">contact</a>
        </div>
      </div>

      <div class="logo__links">
        <div class="logos">
          <a
            class="logo-svg"
            href="https://www.facebook.com/KiltroMusic/"
            target="_blank"
          >
            <img
              src="../static/kiltro/Icons/Rectangle (Colorized).svg"
              class="logo-img"
              alt="Facebook Logo"
            />
          </a>
          <a class="logo-svg" href="https://x.com/KiltroMusic" target="_blank">
            <img
              src="../static/kiltro/Icons/Rectangle (Colorized) (Colorized).svg"
              class="logo-img"
              alt="Twitter Logo"
            />
          </a>
          <a
            class="logo-svg"
            href="https://www.youtube.com/channel/UCf-6irEz-N1twQFUlSGQOuQ"
            target="_blank"
          >
            <img
              src="../static/kiltro/Icons/Rectangle (Colorized)-1.svg"
              class="logo-img"
              alt="Spotify Logo"
            />
          </a>
          <a
            class="logo-svg"
            href="https://open.spotify.com/artist/27CC3tpq7WQR25M03jKTZm"
            target="_blank"
          >
            <img
              src="../static/kiltro/Icons/Rectangle (Colorized)-2.svg"
              class="logo-img"
              alt="Youtube Logo"
            />
          </a>
          <a
            class="logo-svg"
            href="https://www.instagram.com/kiltromusic/"
            target="_blank"
          >
            <img
              src="../static/kiltro/Icons/Rectangle (Colorized)-3.svg"
              class="logo-img"
              alt="Instagram Logo"
            />
          </a>
        </div>
      </div>
    </nav>`;

  document.body.insertAdjacentHTML("afterbegin", nav);
}
