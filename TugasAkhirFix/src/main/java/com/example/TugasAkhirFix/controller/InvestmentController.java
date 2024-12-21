package com.example.TugasAkhirFix.controller;

import com.example.TugasAkhirFix.model.InvestmentForm;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import org.springframework.web.client.RestTemplate;

@Controller
public class InvestmentController {

    @GetMapping("/investment")
    public String showForm(Model model) {
        model.addAttribute("investmentForm", new InvestmentForm());
        return "investmentForm";
    }

    @PostMapping("/investment")
    public String submitForm(InvestmentForm investmentForm, Model model) {
        RestTemplate restTemplate = new RestTemplate();
        String pythonApiUrl = "http://localhost:5000/process"; // URL Flask API

        // Kirim data ke Flask
        String response = restTemplate.postForObject(pythonApiUrl, investmentForm, String.class);
        
        // Parsing JSON response
        JSONObject jsonResponse = new JSONObject(response);
        String imagePath = jsonResponse.getString("image_path");

        model.addAttribute("result", jsonResponse);
        model.addAttribute("imagePath", imagePath);
        return "result"; // Halaman untuk menampilkan hasil
    }
}
