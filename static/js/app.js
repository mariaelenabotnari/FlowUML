document.addEventListener('DOMContentLoaded', function() {
    const editor = document.getElementById('dsl-editor');
    const lineNumbers = document.getElementById('line-numbers');
    const generateBtn = document.getElementById('generate-btn');
    const downloadBtn = document.getElementById('download-btn');
    const diagramImage = document.getElementById('diagram-image');
    const placeholder = document.getElementById('placeholder');
    const errorContainer = document.getElementById('error-container');
    const loadingSpinner = document.getElementById('loading-spinner');
    const exampleBtn = document.getElementById('example-btn');
    const processingTime = document.getElementById('processing-time');
    const timeValue = document.getElementById('time-value');
    const diagramContainer = document.getElementById('diagram-container');
    
    const zoomInBtn = document.getElementById('zoom-in-btn');
    const zoomOutBtn = document.getElementById('zoom-out-btn');
    const zoomResetBtn = document.getElementById('zoom-reset-btn');
    const zoomLevelSpan = document.getElementById('zoom-level');
    
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    let currentZoom = 1;
    const maxZoom = 3;
    const minZoom = 0.5;
    const zoomStep = 0.1;
    let isPanning = false;
    let startPanPosition = { x: 0, y: 0 };
    let currentPanPosition = { x: 0, y: 0 };
    
    function setupDiagramWrapper() {
        let wrapper = document.querySelector('.diagram-wrapper');
        
        if (!wrapper) {
            wrapper = document.createElement('div');
            wrapper.className = 'diagram-wrapper';
            
            if (diagramImage.parentNode) {
                diagramImage.parentNode.insertBefore(wrapper, diagramImage);
                wrapper.appendChild(diagramImage);
            }
        }
        
        return wrapper;
    }
    
    function updateZoomLevel() {
        zoomLevelSpan.textContent = `${Math.round(currentZoom * 100)}%`;
    }
    
    function applyZoom() {
        diagramImage.style.transform = `scale(${currentZoom}) translate(${currentPanPosition.x}px, ${currentPanPosition.y}px)`;
        
        const wrapper = document.querySelector('.diagram-wrapper');
        if (wrapper) {
            if (currentZoom > 1) {
                wrapper.classList.add('zoomed-in');
            } else {
                wrapper.classList.remove('zoomed-in');
                currentPanPosition = { x: 0, y: 0 };
                diagramImage.style.transform = `scale(${currentZoom})`;
            }
        }
        
        updateZoomLevel();
    }
    
    zoomInBtn.addEventListener('click', function() {
        if (currentZoom < maxZoom) {
            currentZoom = Math.min(currentZoom + zoomStep, maxZoom);
            applyZoom();
        }
    });
    
    zoomOutBtn.addEventListener('click', function() {
        if (currentZoom > minZoom) {
            currentZoom = Math.max(currentZoom - zoomStep, minZoom);
            applyZoom();
        }
    });
    
    zoomResetBtn.addEventListener('click', function() {
        currentZoom = 1;
        currentPanPosition = { x: 0, y: 0 };
        applyZoom();
    });
    
    diagramContainer.addEventListener('wheel', function(e) {
        if (diagramImage.style.display === 'none') return;
        
        e.preventDefault();
        
        if (e.deltaY < 0 && currentZoom < maxZoom) {
            currentZoom = Math.min(currentZoom + zoomStep, maxZoom);
        } else if (e.deltaY > 0 && currentZoom > minZoom) {
            currentZoom = Math.max(currentZoom - zoomStep, minZoom);
        }
        
        applyZoom();
    }, { passive: false });
    
    function startPan(e) {
        if (currentZoom <= 1) return;
        
        isPanning = true;
        startPanPosition = {
            x: e.clientX - currentPanPosition.x,
            y: e.clientY - currentPanPosition.y
        };
        
        document.querySelector('.diagram-wrapper').classList.add('panning');
    }
    
    function movePan(e) {
        if (!isPanning) return;
        
        currentPanPosition = {
            x: (e.clientX - startPanPosition.x) / currentZoom,
            y: (e.clientY - startPanPosition.y) / currentZoom
        };
        
        diagramImage.style.transform = `scale(${currentZoom}) translate(${currentPanPosition.x}px, ${currentPanPosition.y}px)`;
    }
    
    function endPan() {
        isPanning = false;
        document.querySelector('.diagram-wrapper')?.classList.remove('panning');
    }
    
    diagramContainer.addEventListener('mousedown', startPan);
    diagramContainer.addEventListener('mousemove', movePan);
    diagramContainer.addEventListener('mouseup', endPan);
    diagramContainer.addEventListener('mouseleave', endPan);
    
    function updateLineNumbers() {
        const lines = editor.value.split('\n').length;
        lineNumbers.innerHTML = Array(lines)
            .fill(0)
            .map((_, i) => `<div>${i + 1}</div>`)
            .join('');
    }
    
    editor.addEventListener('input', updateLineNumbers);
    editor.addEventListener('scroll', function() {
        lineNumbers.scrollTop = editor.scrollTop;
    });
    
    const exampleCode = `sequence ComprehensiveExample {
    actor User;
    object Client;
    boundary UI;
    control Controller;
    entity Order;
    database Database;
    
    User -> UI : Select_product;
    UI => Controller : Notify_selection;
    Controller -> Database : Query_product_details;
    Database --> Controller : Return_product_data;
    Controller -> UI : Update_display;
    
    for (each_item_in_cart) {
        User -> UI : Adjust_quantity;
        UI -> Controller : Update_item_count;
        Controller -> Order : Recalculate_total;
    }
    
    alt {
        case (checkout_as_guest) {
            User -> UI : Proceed_as_guest;
            UI -> Controller : Process_guest_checkout;
        }
        case (checkout_as_member) {
            User -> UI : Login;
            UI -> Controller : Authenticate_user;
            Controller -> Database : Verify_credentials;
            Database --> Controller : Authentication_result;
            
            Controller -x> UI : Show_error_message;
        }
    }
    
    opt (apply_coupon) {
        User -> UI : Enter_coupon_code;
        UI -> Controller : Validate_coupon;
        Controller -> Database : Check_coupon_validity;
        Database --> Controller : Coupon_status;
        Controller -> Order : Apply_discount;
    }
    
    User -> Controller : Place_order;
    Controller activate;
    Controller -> Order : Create_new_order;
    Order activate;
    Order -> Database : Save_order_details;
    
    Controller <-> Order : Synchronize_order_status;
    Controller -o> Database : Request_with_timeout;
    
    Database |< Controller : Bulk_data_transfer;
    
    Order deactivate;
    Controller deactivate;
}`;
    
    exampleBtn.addEventListener('click', function() {
        editor.value = exampleCode;
        updateLineNumbers();
    });
    
    generateBtn.addEventListener('click', function() {
        const dslText = editor.value.trim();
        if (!dslText) {
            errorContainer.textContent = "Please enter DSL code.";
            errorContainer.style.display = 'block';
            return;
        }
        
        loadingSpinner.style.display = 'inline-block';
        generateBtn.disabled = true;
        errorContainer.style.display = 'none';
        processingTime.style.display = 'none';
        
        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ dsl_text: dslText })
        })
        .then(response => response.json())
        .then(data => {
            loadingSpinner.style.display = 'none';
            generateBtn.disabled = false;
            
            if (data.success) {
                setupDiagramWrapper();
                
                currentZoom = 1;
                currentPanPosition = { x: 0, y: 0 };
                updateZoomLevel();
                
                diagramImage.src = 'data:image/png;base64,' + data.image;
                diagramImage.style.display = 'block';
                diagramImage.style.transform = 'scale(1)';
                placeholder.style.display = 'none';
                
                downloadBtn.disabled = false;
                
                if (data.processing_time) {
                    timeValue.textContent = data.processing_time;
                    processingTime.style.display = 'inline-block';
                }
            } else {
                errorContainer.textContent = data.error || 'An error occurred.';
                if (data.traceback) {
                    errorContainer.textContent += '\n\n' + data.traceback;
                }
                errorContainer.style.display = 'block';
            }
        })
        .catch(error => {
            loadingSpinner.style.display = 'none';
            generateBtn.disabled = false;
            errorContainer.textContent = 'Network error: ' + error.message;
            errorContainer.style.display = 'block';
        });
    });
    
    downloadBtn.addEventListener('click', function() {
        if (diagramImage.src) {
            const link = document.createElement('a');
            link.download = 'sequence_diagram.png';
            link.href = diagramImage.src;
            link.click();
        }
    });
    
    document.addEventListener('keydown', function(e) {
        if (diagramImage.style.display === 'none') return;
        
        if (e.ctrlKey && e.key === '+') {
            e.preventDefault();
            if (currentZoom < maxZoom) {
                currentZoom = Math.min(currentZoom + zoomStep, maxZoom);
                applyZoom();
            }
        }
        
        if (e.ctrlKey && e.key === '-') {
            e.preventDefault();
            if (currentZoom > minZoom) {
                currentZoom = Math.max(currentZoom - zoomStep, minZoom);
                applyZoom();
            }
        }
        
        if (e.ctrlKey && e.key === '0') {
            e.preventDefault();
            currentZoom = 1;
            currentPanPosition = { x: 0, y: 0 };
            applyZoom();
        }
    });
    
    updateLineNumbers();
}); 