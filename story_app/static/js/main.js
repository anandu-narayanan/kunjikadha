document.addEventListener('DOMContentLoaded', () => {
    enableButtonRipples();
    enhanceStoryForm();
    setupStoryPreview();
});

function enableButtonRipples() {
    document.addEventListener('click', (event) => {
        const element = event.target.closest('.btn, .choice-btn');
        if (!element) {
            return;
        }

        createRipple(event, element);
    });
}

function createRipple(event, element) {
    const ripple = document.createElement('span');
    const rect = element.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);

    ripple.className = 'btn-ripple';
    ripple.style.width = `${size}px`;
    ripple.style.height = `${size}px`;
    ripple.style.left = `${event.clientX - rect.left - (size / 2)}px`;
    ripple.style.top = `${event.clientY - rect.top - (size / 2)}px`;

    element.appendChild(ripple);
    window.setTimeout(() => ripple.remove(), 550);
}

function enhanceStoryForm() {
    const form = document.getElementById('storyForm');
    const submitButton = document.getElementById('createBtn');

    if (!form || !submitButton) {
        return;
    }

    form.addEventListener('submit', (event) => {
        const characterInput = form.querySelector('[name="character"]');
        const placeInput = form.querySelector('[name="place"]');
        const character = characterInput ? characterInput.value.trim() : '';
        const place = placeInput ? placeInput.value.trim() : '';

        if (!character || !place) {
            event.preventDefault();
            showFloatingMessage('Please fill in the character and place first.');

            if (!character && characterInput) {
                characterInput.focus();
            } else if (placeInput) {
                placeInput.focus();
            }
            return;
        }

        const label = submitButton.querySelector('.btn-label');
        if (label) {
            submitButton.dataset.originalLabel = label.textContent;
            label.textContent = 'Creating your story...';
        }

        submitButton.disabled = true;
        submitButton.classList.add('is-loading');

        window.setTimeout(() => {
            if (!submitButton.isConnected) {
                return;
            }

            const originalLabel = submitButton.dataset.originalLabel;
            if (label && originalLabel) {
                label.textContent = originalLabel;
            }

            submitButton.disabled = false;
            submitButton.classList.remove('is-loading');
        }, 12000);

        if (typeof confetti !== 'undefined') {
            confetti({
                particleCount: 70,
                spread: 60,
                origin: { y: 0.68 },
                colors: ['#ff7b5b', '#f5c24e', '#1eb6a5', '#6ab7ff']
            });
        }
    });
}

function setupStoryPreview() {
    const characterInput = document.querySelector('[name="character"]');
    const placeInput = document.querySelector('[name="place"]');
    const themeInput = document.querySelector('[name="theme"]');
    const previewCharacter = document.getElementById('previewCharacter');
    const previewPlace = document.getElementById('previewPlace');
    const previewTheme = document.getElementById('previewTheme');
    const previewProgress = document.getElementById('previewProgress');
    const previewProgressText = document.getElementById('previewProgressText');
    const previewCard = document.querySelector('.story-preview-card');
    const stepChips = document.querySelectorAll('.step-chip[data-step]');

    if (!characterInput || !placeInput || !themeInput || !previewCharacter || !previewPlace || !previewTheme) {
        return;
    }

    const updatePreview = () => {
        const character = characterInput.value.trim();
        const place = placeInput.value.trim();
        const themeValue = themeInput.value.trim();
        const selectedTheme = themeInput.options[themeInput.selectedIndex];
        const themeLabel = selectedTheme ? selectedTheme.textContent.trim() : '';

        previewCharacter.textContent = character || 'Your hero appears here';
        previewPlace.textContent = place ? `${place} is ready for the adventure.` : 'Choose a place to begin the adventure.';
        previewTheme.textContent = themeLabel || 'Pick a fun theme';
        previewTheme.dataset.theme = themeValue || 'default';

        const filledCount = [character, place, themeValue].filter(Boolean).length;
        const progress = (filledCount / 3) * 100;

        if (previewProgress) {
            previewProgress.style.width = `${progress}%`;
        }

        if (previewProgressText) {
            if (filledCount === 3) {
                previewProgressText.textContent = 'Story magic is ready. Press create!';
            } else if (filledCount === 2) {
                previewProgressText.textContent = 'One more sparkle and the story is ready.';
            } else if (filledCount === 1) {
                previewProgressText.textContent = 'Great start. Add two more details.';
            } else {
                previewProgressText.textContent = 'Fill all 3 steps to unlock your story magic.';
            }
        }

        if (previewCard) {
            previewCard.dataset.ready = filledCount === 3 ? 'true' : 'false';
        }

        stepChips.forEach((chip) => {
            const stepName = chip.dataset.step;
            const isReady =
                (stepName === 'character' && !!character) ||
                (stepName === 'place' && !!place) ||
                (stepName === 'theme' && !!themeValue);
            chip.classList.toggle('is-ready', isReady);
        });
    };

    characterInput.addEventListener('input', updatePreview);
    placeInput.addEventListener('input', updatePreview);
    themeInput.addEventListener('change', updatePreview);
    updatePreview();
}

function showFloatingMessage(message) {
    const toast = document.createElement('div');
    toast.className = 'floating-error';
    toast.textContent = message;
    document.body.appendChild(toast);

    window.setTimeout(() => {
        toast.remove();
    }, 3000);
}
