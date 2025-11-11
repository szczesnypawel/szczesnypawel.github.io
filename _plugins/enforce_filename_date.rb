# Jekyll plugin to enforce post date from filename
# This ensures that the published date always matches the date in the filename
# Format expected: YYYY-MM-DD-title.markdown

Jekyll::Hooks.register :posts, :post_init do |post|
  # Extract date from filename
  # Jekyll post filenames are typically: YYYY-MM-DD-title.markdown
  filename = File.basename(post.path)
  
  # Match the date pattern at the beginning of the filename
  date_match = filename.match(/^(\d{4})-(\d{2})-(\d{2})-/)
  
  if date_match
    year = date_match[1].to_i
    month = date_match[2].to_i
    day = date_match[3].to_i
    
    begin
      # Create a new date object from the filename
      filename_date = Time.utc(year, month, day)
      
      # Override the date with the filename date
      post.data['date'] = filename_date
      post.date = filename_date
      
      Jekyll.logger.debug "FilenameDateEnforcer:", "Set date for #{filename} to #{filename_date.strftime('%Y-%m-%d')}"
    rescue ArgumentError => e
      Jekyll.logger.warn "FilenameDateEnforcer:", "Invalid date in filename #{filename}: #{e.message}"
    end
  else
    Jekyll.logger.warn "FilenameDateEnforcer:", "Could not extract date from filename: #{filename}"
  end
end


