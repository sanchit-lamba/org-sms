(require 'org)

; replace the PATH_TO_CURRENT_DIRECTORY with the current directory

(setq a "PATH_TO_CURRENT_DIRECTORY/org-agenda.txt")

(org-agenda-list)

(org-agenda-day-view)

(org-agenda-write a)

