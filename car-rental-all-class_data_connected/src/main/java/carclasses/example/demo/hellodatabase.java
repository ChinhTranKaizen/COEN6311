package carclasses.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@Component
@RestController
public class hellodatabase {
  
  @Autowired
    JdbcTemplate jdbcTemplate;
  
  @RequestMapping(value="/hello", method=RequestMethod.GET)
    public String index() {
    
    String sql = "SELECT phone FROM customers WHERE customer_id = ?";
    
    // Query the database through jdbcTemplate
    String phone = (String)jdbcTemplate.queryForObject(
        sql, new Object[] { 2 }, String.class);
    
        return "Hello " + phone;
    }

  }