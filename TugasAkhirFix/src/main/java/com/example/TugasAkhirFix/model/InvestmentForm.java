package com.example.TugasAkhirFix.model;

public class InvestmentForm {

    private double initialPrice; // Harga Awal
    private double finalPrice;   // Harga Akhir
    private double marketVolume;  // Volume Pasar

    // Getters and Setters
    public double getInitialPrice() {
        return initialPrice;
    }

    public void setInitialPrice(double initialPrice) {
        this.initialPrice = initialPrice;
    }

    public double getFinalPrice() {
        return finalPrice;
    }

    public void setFinalPrice(double finalPrice) {
        this.finalPrice = finalPrice;
    }

    public double getMarketVolume() {
        return marketVolume;
    }

    public void setMarketVolume(double marketVolume) {
        this.marketVolume = marketVolume;
    }
}
