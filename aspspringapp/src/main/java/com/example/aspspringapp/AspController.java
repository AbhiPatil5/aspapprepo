package com.example.aspspringapp;

import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AspController {
    
    private final MeterRegistry meterRegistry;

    @Autowired
    public AspController(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
    }
    
    @GetMapping("/")
    public String asp() {
        meterRegistry.counter("custom_hello_counter").increment();
        return "hello";
    }
}