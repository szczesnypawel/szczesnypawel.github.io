# Keep the auto-generated tag/category archive pages out of the sitemap and
# search results: on a personal site they are thin pages that compete with the
# profile pages for searches on the author's name.
Jekyll::Hooks.register :site, :pre_render do |site|
  site.pages.each do |page|
    next unless page.url.start_with?('/tags/', '/categories/')

    page.data['sitemap'] = false
    page.data['noindex'] = true
  end
end
