cat match_links | grep -oE 'https?://[^[:space:]]+' | sed 's/".*$//' >  solo_match_links
