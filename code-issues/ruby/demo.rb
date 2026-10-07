# S1192: String literal duplicated more than 3 times — should be a constant
def format_response(status)
  if status == "active"
    puts "Processing request..."
    puts "Processing request..."
    puts "Processing request..."
    puts "Processing request..."
  end
end

# S1481: Local variable assigned but never used
def compute_total(items)
  unused_discount = 0.15
  items.sum { |i| i[:price] } * 1.08
end

# S3776: Cognitive complexity too high — excessive nesting
def evaluate(a, b, c, d, e)
  if a
    if b
      if c
        if d
          if e
            if a && b
              return "deep match"
            end
          end
        end
      end
    end
  end
  "no match"
end
