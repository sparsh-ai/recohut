import React from 'react';
import LiteYouTubeEmbed from 'react-lite-youtube-embed';
import 'react-lite-youtube-embed/dist/LiteYouTubeEmbed.css';

export default function YouTube({vid, title}) {
    return (
        <div className="video-container">
            <LiteYouTubeEmbed
                id={vid}
                params="autoplay=1&autohide=1&showinfo=0&rel=0"
                title={title}
                poster="maxresdefault"
                webp
            />
            <br />
        </div>
    );
  }