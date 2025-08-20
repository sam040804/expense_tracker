<script>
    // Get expenses from Flask
    const expenses = {{ expenses|tojson }};

    // Extract unique categories
    const categories = [...new Set(expenses.map(e => e.category))];

    // Sum amounts per category
    const amounts = categories.map(cat => 
        expenses.filter(e => e.category === cat).reduce((sum, e) => sum + e.amount, 0)
    );

    // Generate dynamic colors
    const colors = categories.map((_, i) => `hsl(${i * 60 % 360}, 70%, 60%)`);

    const ctx = document.getElementById('expenseChart').getContext('2d');

    // Destroy existing chart if it exists
    if (window.expChart) window.expChart.destroy();

    // Create pie chart
    window.expChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: categories,
            datasets: [{
                label: 'Expenses by Category',
                data: amounts,
                backgroundColor: colors,
                borderColor: '#fff',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { padding: 15 }
                },
                tooltip: { enabled: true }
            }
        }
    });
</script>
